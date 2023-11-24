import json

class Config:
    IP_RANGE    = '192.168.2.0/24'
    DEVICE_FILE = 'devices.txt'
    PORT        = 9090

    @classmethod
    def read_config_file(cls, config_filename:str):
        with open(config_filename, 'r') as f:
            config = json.load(f)
            Config.IP_RANGE     = config['IP_RANGE'] 
            Config.DEVICE_FILE  = config['DEVICE_FILE']
            Config.PORT         = config['PORT']

    @classmethod
    def write_config_file(cls, config_filename:str):
        with open(config_filename, 'w') as f:
            result = dict()
            result['IP_RANGE']      = Config.IP_RANGE
            result['DEVICE_FILE']   = Config.DEVICE_FILE
            result['PORT']          = Config.PORT
            json.dump(result, fp=f, indent=4)

if __name__ == '__main__':
    from constant import Constants
    Config.write_config_file(Constants.CONFIG_FILENAME)