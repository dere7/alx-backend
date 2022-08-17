import createPushNotificationsJobs from './8-job';
import Kue from 'kue';
import { assert, expect } from 'chai';

describe('createPushNotificationsJobs', function () {
  let queue = null;
  before(function () {
    queue = Kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('display a error message', () => {
    assert.throw(() => createPushNotificationsJobs('notArray', queue), Error, 'Jobs is not an array');
  });

  it('create new jobs', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.be.equal(1);
    expect(queue.testMode.jobs[0].data).to.deep.equal(list[0]);
  });
});
