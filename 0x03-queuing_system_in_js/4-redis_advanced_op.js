import redis from 'redis';
import { reply_in_order } from 'redis/lib/utils';
import util from 'util';

// create redis client

const client = redis.createClient();

client.on('connect', async () => {
	console.log('Redis client connected to the server');
	const hashKey = 'Holbertonschools'
	const values = {
			'Portland': 50,
    	'Seattle': 80,
    	'New York': 20,
    	'Bogota': 20,
    	'Cali': 40,
    	'Paris': 2,
		}
	function createHash(hasKey, values){
		client.hmset(hasKey, values, redis.print);
	}
	function getHash(hashKey){
		client.hgetall(hashKey, (err, reply) =>{
			if (err){
				console.log(err);
			} else{
				console.log(reply);
			}
		});
	}
	createHash(hashKey, values);
	getHash(hashKey);
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`);
});
