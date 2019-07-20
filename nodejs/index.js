const sensor = require('ds18b20-raspi');
const Influx = require('influxdb-nodejs');

const INFLUX_HOST = process.env.INFLUX_HOST || '127.0.0.1'
const INFLUX_PORT = process.env.INFLUX_PORT || 8086
const INFLUX_DB = process.env.INFLUX_DB || 'mydb'


// Set up Influx Connection and schema
const client = new Influx(`http://${INFLUX_HOST}:${INFLUX_PORT}/${INFLUX_DB}`);

const fieldSchema = {
    value: 'i'
  };

  // Not sure what this is about tbh, but the examples have it in so no harm I guess for now..
  const tagSchema = {
    spdy: ['sensor'],
    method: '*',
    // http stats code: 10x, 20x, 30x, 40x, 50x
    type: ['1', '2', '3', '4', '5'],
  };

client.schema('http', fieldSchema, tagSchema, {
    // default is false
    stripUnknown: true,
}); 


// Now get the value from the sensor:
// Only works with a single sensor for the moment in time, I just want to see if this even works
// It will just find the first sensor connected to the pi


function SendTemptoInflux(client){
  const SENSOR_VAL = sensor.readSimpleC();
  console.log(`${SENSOR_VAL} degC`);
  
  client.write('http')
    .tag({
      spdy: 'sensor',
      method: 'GET',
      type: '1',  
    })
    .field({
      value: SENSOR_VAL
    })
    .then(() => console.info('write point success'))
    .catch(console.error);
}

setInterval(function() {
  SendTemptoInflux(client);
}, 5000);
