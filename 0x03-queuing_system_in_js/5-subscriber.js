import redis from 'redis';

const subscriber = redis.createClient();
const channel = 'holberton school channel';

subscriber.on('connect', function () {
  console.log('Redis client connected to the server');
});

subscriber.on('error', function (err) {
  console.log('Redis client not connected to the server: ', err.message);
});

subscriber.subscribe(channel);

subscriber.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  }
  console.log(message);
});
