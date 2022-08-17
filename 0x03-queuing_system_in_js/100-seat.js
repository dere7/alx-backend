import express from 'express';
import Kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const queue = Kue.createQueue();
let reservationEnabled = true;
reserveSeat(50);

async function reserveSeat (number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const res = await getAsync('available_seats');
  return res;
}

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: seats });
  res.end();
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled) {
    queue.createJob('reserve_seat').save()
      .on('enqueue', () => {
        res.send({ status: 'Reservation in process' });
        res.end();
      }).on('error', (err) => {
        console.log(`Seat reservation job JOB_ID failed: ${err.message()}`);
        res.send({ status: 'Reservation failed' });
        res.end();
      }).on('complete', (res) => console.log('Seat reservation job JOB_ID completed', res));
  } else {
    res.send({ status: 'Reservation are blocked' });
    res.end();
  }
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', (job, done) => {
    (async () => {
      let availableSeats = await getCurrentAvailableSeats();
      await reserveSeat(--availableSeats);
      if (availableSeats === 0) {
        reservationEnabled = false;
      } else if (availableSeats < 0) {
        const err = new Error('Not enough seats available');
        job.failed().error(err);
        done(err);
      }
    })();
  });
  res.send({ status: 'Queue processing' });
  res.end();
});

app.listen(1245);
