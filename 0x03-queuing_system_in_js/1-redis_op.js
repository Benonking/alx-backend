import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
	
	function setNewSchool(schoolName, value){
		client.set(schoolName, value,redis.print);
		//console.log(`Setting value ${value} for key ${schoolName}`);
		}
	function displaySchoolValue(schoolName) {
		client.get(schoolName, (err, reply) => {
			if (err) {
				console.log(`Error getting value for key ${schoolName}: ${err}`);
			} else {
				console.log(reply);
			}
		});
		
	}
	displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	displaySchoolValue('HolbertonSanFrancisco');
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`);
});
