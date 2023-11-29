import { createQueue } from "kue";
const queue = createQueue();


function sendNotfication(phoneNumber, message, job, done){
	console.log(`sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
	const {phoneNumber, message} = job.data;
	sendNotfication(phoneNumber,message);
	done();
})