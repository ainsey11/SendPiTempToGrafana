sudo apt-get update

sudo apt-get install influxdb -y

sudo apt-get install influxdb-client -y

npm install -f 

edit /etc/influxdb/influx.conf

uncomment lines 207,209 and 212

run sudo systemctl restart influxdb

run the command : influx

once in the influx shell, run : 

create database mydb

exit database (ctrl+d)

change the variables to your influxdb server IP (or 127.0.0.1 if running on the same pi as the sensor)

run node index.js
