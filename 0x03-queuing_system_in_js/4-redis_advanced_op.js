import redis from 'redis';

const client = redis.createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log('Redis client not connected to the server: ', err.message);
});

client.hset('HolbertonSchools',
  'Portland', 50,
  'Seattle', 80,
  'New York', 20,
  'Bogota', 20,
  'Cali', 40,
  'Paris', 2,
  redis.print);

client.hgetall('HolbertonSchools', (_, v) => console.log(v));
