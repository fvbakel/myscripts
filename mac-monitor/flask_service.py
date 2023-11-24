from flask import Flask
from flask import request
from device_monitor import *
from config import Config
from constant import Constants
import json

monitor = DeviceMonitor()

app = Flask(__name__)

@app.route("/refresh")
def refresh():
    monitor.refresh()
    return json.dumps(Constants.OK)

@app.route("/monitor")
def last_refresh():
    result = dict()
    result['last_refresh'] = str(monitor.last_refresh)
    result['seconds_since_last_refresh'] = monitor.seconds_since_last_refresh
    return json.dumps(result)

@app.route("/devices/")
def devices():
    fields = request.args.get('fields',default=None,type=str)
    if fields is None:
        return json.dumps(list(monitor.id_vs_device.keys()))
    
    fields_set = set(fields.split(','))
    result = []
    for device in monitor.devices.values():
        device_values = {key: device.str_dict()[key] for key in fields_set} 
        result.append(device_values)
    return json.dumps(result)


@app.route("/devices/<device_id>")
def show_device(device_id):
    if not device_id in monitor.id_vs_device:
        return ''
    device = monitor.id_vs_device[device_id]
    return json.dumps(device.str_dict())

if __name__ == '__main__':
    Config.read_config_file(Constants.CONFIG_FILENAME)
    monitor.set_devices(Config.DEVICE_FILE)
    monitor.refresh()
    app.run(host='0.0.0.0', port=Config.PORT)