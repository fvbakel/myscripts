from device_monitor import *
from config import Config
import json


def test_to_json():
    device = Device('a','b','c')
    device.last_seen = datetime.datetime.now()
    print(json.dumps(device.str_dict()))

def test_DeviceMonitor():
    monitor = DeviceMonitor()
    monitor.set_devices(Config.DEVICE_FILE)
    monitor.refresh()
    for device in monitor.devices.values():
        print(f'device {device.display_name} {device.last_seen}')

if __name__ == '__main__':  
    #test_to_json()
    test_DeviceMonitor()