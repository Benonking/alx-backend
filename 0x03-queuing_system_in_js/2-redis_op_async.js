import redis from 'redis';
import util from 'util';

// create redis client

const client = redis.createClient();

// Promisify the get method
const getAsync = util.promisify(client.get).bind(client)

client.on('connect', async () => {
	console.log('Redis client connected to the server');
	
	function setNewSchool(schoolName, value){
		client.set(schoolName, value,redis.print);
		//console.log(`Setting value ${value} for key ${schoolName}`);
		}
	async function displaySchoolValue(schoolName) {
		try {
			const reply = await getAsync(schoolName);
			console.log(reply);
		} catch (err) {
			console.log(err);
		}
	}
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`);
});
