import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
client.get = promisify(client.get).bind(client);

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log('Redis client not connected to the server: ', err.message);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await client.get(schoolName);
    console.log(reply);
  } catch (e) {
    console.error(e);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
