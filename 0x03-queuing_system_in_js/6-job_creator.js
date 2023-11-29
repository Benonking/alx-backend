import { createQueue } from "kue";

const queue = createQueue();

const jobData = {
  phoneNumber: '078199',
  message: 'call me',
};
	// cretae job
const jobQueue = queue.create('push_notification_code', jobData).save((err) => {
	if (err) {
		throw new Error('Nofification job failed');
	} else {
		console.log(`Notification job created: ${jobQueue.id}`);
	}
});

jobQueue.on('complete', () => {
	console.log('Notification job completed');
});
jobQueue.on('failed', (err) => {
	console.error(err);
});