# mac-monitor

This program keeps track of when a list of specific mac address has been last seen on your local network. The intention to provide this a a rest service to other devices and apps.

## Background

This script is based on nmap and the file /proc/net/arp

To get a IP address with nmap requires root aces. However, this information can also be retrieved from /proc/net/arp. 
However, this file is only up to date after a nmap scan


## Rest API

The REST API is Flask based. The table below list the available REST requests.

| Route |  Example | Result |
|---|---|---|
| /refresh | <http://127.0.0.1:9090/refresh>  | Rescan. This can take a while |
| /monitor  | <http://127.0.0.1:9090/monitor> | Last update info of the monitor |
| /devices | <http://127.0.0.1:9090/devices/> | list of device id's |
| /devices?fields=<> | <http://127.0.0.1:9090/devices/?fields=id,time_since_seen_sec> | For each device, output the given fields  |
| /devices/<id> | <http://127.0.0.1:9090/devices/aa> | Output all fields of the given device |

All output is in JSON format.

## Generate a default config file

The command below will create the default config file monitor.json. This file can be updated to your needs. Note that it will overwrite any existing file!

```
python3 config.py
```

## Devices file

The devices file is used to configure the devices you want to monitor.

Example of a ```devices.txt``` file:

```
fa:11:23:21:2e:9e|aa|Device 1
3a:56:7c:fc:c8:dc|bb|Device 2
```

## Installation steps

Take the following steps to install.

- ```sudo apt-get install nmap python3-flask python3-nmap```
- copy this directory to your target
- ```python3 config.py```
- update monitor.json to your needs
- create devices.txt to your needs (see format above)
- Test the installation to this point. The command should output the device information to the console.
- ```python3 python3 test_device_monitor.py```
- Now we are ready to run the service in the console
- ```python3 flask_service.py```
- Test the Rest service is now available

## Install as a service 

- ```sudo cp mac-monitor.service /etc/systemd/system/```
- edit path in ```/etc/systemd/system/mac-monitor.service```
- 