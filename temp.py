#!/usr/bin/python
#loading up modules
from w1thermsensor import W1ThermSensor
import os
import time
from influxdb.influxdb08 import InfluxDBClient

while True:

        sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041501a634ff")
        sensor1_val = sensor1.get_temperature()

        sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041501aedaff")
        sensor2_val = sensor2.get_temperature()

        sensor3 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "031501c516ff")
        sensor3_val = sensor3.get_temperature()

        sensor4 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "031501c51fff")
        sensor4_val = sensor4.get_temperature()

        sensor5 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "031501c1e1ff")
        sensor5_val = sensor5.get_temperature()


        print("posting data")


        sensor1_json_body =[
        {
            "name" : "sensor1_temp_c",
            "columns" : ["value", "sensor"],
            "points" : [
              [sensor1_val, "sensor01"]
            ]
          }
        ]

        sensor2_json_body =[
          {
            "name" : "sensor2_temp_c",
            "columns" : ["value", "sensor"],
            "points" : [
              [sensor2_val, "sensor02"]
            ]
          }
        ]

        sensor3_json_body =[
          {
            "name" : "sensor3_temp_c",
            "columns" : ["value", "sensor"],
            "points" : [
              [sensor3_val, "sensor03"]
            ]
          }
        ]

        sensor4_json_body =[
          {
            "name" : "sensor4_temp_c",
            "columns" : ["value", "sensor"],
            "points" : [
              [sensor4_val, "sensor04"]
            ]
          }
        ]

        sensor5_json_body =[
          {
            "name" : "sensor5_temp_c",
            "columns" : ["value", "sensor"],
            "points" : [
              [sensor5_val, "sensor05"]
            ]
          }
        ]


        client = InfluxDBClient('SEVRVERIP', 8086, 'USERNAME', 'PASSWORD', 'DB_NAME')
        client.write_points(sensor1_json_body)
        client.write_points(sensor2_json_body)
        client.write_points(sensor3_json_body)
        client.write_points(sensor4_json_body)
        client.write_points(sensor5_json_body)
        print(sensor1_val)
        print(sensor2_val)
        print(sensor3_val)
        print(sensor4_val)
        print(sensor5_val)
        time.sleep(2)
