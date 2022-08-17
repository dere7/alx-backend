export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach(job => {
    const j = queue.create('push_notification_code_3', job);
    j.save();
    j.on('enqueue', () => console.log(`Notification job created: ${j.id}`))
      .on('complete', () => console.log(`Notification job ${j.id} completed`))
      .on('failed', (err) => console.log(`Notification job ${j.id} failed: ${err}`))
      .on('progress', (progress) => console.log(`Notification job ${j.id} ${progress}% complete`));
  });
}
