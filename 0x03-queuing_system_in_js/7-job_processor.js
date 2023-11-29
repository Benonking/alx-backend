import { createQueue } from "kue";
const queue = createQueue()

const blacklist = ['4153518780', '4153518781'];

function sendNotfication(phoneNumber, message, job, done){
	
	// track progress of the bob
	job.progress(0, 100);
	if (blacklist.includes(phoneNumber)){
		done(Error(`Phone number ${phoneNumber} is blacklisted`));
	}
	job.progress(50,100);
	console.log(`sending notification to ${phoneNumber}, with message: ${message}`);
	done();
}

queue.process('push_notification_code',2, (job, done) => {
	const {phoneNumber, message} = job.data;
	sendNotfication(phoneNumber,message, queue, done);
	done();
});