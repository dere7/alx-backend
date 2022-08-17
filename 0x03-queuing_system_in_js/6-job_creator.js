import kue from 'kue';

const jobData = {
  phoneNumber: '+1983432323',
  message: 'Hello there!'
};

const queue = kue.createQueue();

const job = queue.createJob('push_notification_code', jobData).save();

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
  .on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
