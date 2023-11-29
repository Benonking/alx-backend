import { createQueue } from "kue";
const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
]

jobs.forEach((item) => {
	const jobQueue = queue.create('push_notification_code_2', item).save((err) => {
		if (err){
			throw err;
		} else{
			console.log(`Notification job ${jobQueue.id} completed`)
		}
	});
	jobQueue.on('complete', () =>{
		console.log(`Notification job ${jobQueue.id} completed`);
	});
	jobQueue.on('failed', (err) =>{
		console.log(`Notification job ${jobQueue.id} failed: ${err}`);
	});
	jobQueue.on('progess', (progress) => {
		console.log(`Notification job ${jobQueue.id} ${progress}% complete`)
	});
});