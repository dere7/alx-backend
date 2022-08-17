import Kue from 'kue';

const queue = Kue.createQueue();
const blacklist = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.indexOf(phoneNumber) !== -1) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(err);
    done(err);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
  done(null);
});
