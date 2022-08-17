import Kue from 'kue';

const queue = Kue.createQueue();

function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', ({ data }, done) => {
  sendNotification(data.phoneNumber, data.message);
  done(null);
});
