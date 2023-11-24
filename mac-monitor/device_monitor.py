import nmap
import datetime
from constant import Constants
from config import Config
import json

class Device:

    def __init__(self,id:str,display_name:str, mac:str):
        self.id:str = id
        self.display_name:str = display_name
        self.mac = mac
        self.last_seen:datetime.datetime = None
    
    @property
    def time_since_seen_sec(self):
        if self.last_seen == None:
            return None
        duration = datetime.datetime.now() - self.last_seen
        return int(duration.total_seconds())
    
    def str_dict(self):
        result=self.__dict__.copy()
        result['last_seen'] = str(result['last_seen'])
        result['time_since_seen_sec'] = self.time_since_seen_sec
        return result

class NetInfo:

    def __init__(self):
        self.refresh()

    def refresh(self):
        self.mac_vs_ip: dict[str,str] = dict()
        self.ip_vs_mac: dict[str,str] = dict()

        # IP address       HW type     Flags       HW address            Mask     Device
        with open(Constants.ARP_FILE) as arp_file:
            for line in arp_file:
                if line.startswith('IPaddress'):
                    continue
                ip_address = line[0:14].replace(' ','')
                mac = line[40:62].replace(' ','')
                self.mac_vs_ip[mac] = ip_address
                self.ip_vs_mac[ip_address] = mac

class DeviceMonitor:

    def __init__(self):
        self.devices:dict[str,Device] = dict()
        self.id_vs_device:dict[str,Device] = dict()
        self.scanner = nmap.PortScanner()
        self.net_info = NetInfo()
        self.last_refresh = None

    def add(self,id:str,display_name:str,mac:str):
        if mac in self.devices:
            raise(LookupError(f'Mac {mac} already exists'))
        self.devices[mac] = Device(id,display_name,mac)
        self.id_vs_device[id] = self.devices[mac]

    def set_devices(self,file:str):
        with open(file) as device_file:
            for line in device_file:
                fields = line.split('|')
                self.add(fields[1],fields[2],fields[0])

    def refresh(self):
        self.scanner.scan(hosts=Config.IP_RANGE, arguments='-sP')
        self.net_info.refresh()
        host_list = self.scanner.all_hosts()
        for host in host_list:
            if 'ipv4' in self.scanner[host]['addresses']:
                ip_address = self.scanner[host]['addresses']['ipv4']
                if ip_address in self.net_info.ip_vs_mac:
                    mac = self.net_info.ip_vs_mac[ip_address]
                    if mac in self.devices:
                        self.devices[mac].last_seen = datetime.datetime.now()
        self.last_refresh = datetime.datetime.now()

    @property
    def seconds_since_last_refresh(self):
        if self.last_refresh == None:
            return None
        duration = datetime.datetime.now() - self.last_refresh
        return int(duration.total_seconds()) 
