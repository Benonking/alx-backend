import redis from 'redis';
//import { reply_in_order } from 'redis/lib/utils';
//import util from 'util';

// create redis client


const subscriber = redis.createClient();

subscriber.on('connect', async () => {
	console.log('Redis client connected to the server');
	subscriber.subscribe('holberton school channel');
});
subscriber.on('message', (channel, message) => {
	console.log(message);
	if(message === 'KILL_SERVER') {
		subscriber.unsubscribe('holberton school channel');
		subscriber.quit()
	}
});

subscriber.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`);
});
