
function createPushNotifications(jobs, queue){
	if (!Array.isArray(jobs)){
		throw new Error('Jobs is not an array');
	}
	jobs.forEach(element => {
		const job = queue.create('push_notification_code_3', element).save((err) => {
			if(err) {
				throw err;
			} else {
				console.log(`Notification job created: ${job.id}`);
			}
		});
			job.on('complete', () => {
				console.log(`Notification job ${job.id} completed`);;
			});
			job.on('fail', (err) => {
				console.log(`Notification job ${job.id} failed: ${err}`);
			});
			job.on('progress', (progress) => {
				console.log(`Notification job ${job.id} ${progress}% complete`);
			});
		});
}
module.exports = createPushNotifications