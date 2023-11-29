import redis from 'redis';
//import { reply_in_order } from 'redis/lib/utils';
//import util from 'util';

// create redis client


const publisher = redis.createClient();

publisher.on('connect', async () => {
	console.log('Redis client connected to the server');
	
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
}); 
function publishMessage(message, time) {
	// handle sleep
	setTimeout(() => {
		console.log(`About to send ${message}`);
		publisher.publish('holberton school channel', message);
	}, time);
	}
publisher.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`);
});
