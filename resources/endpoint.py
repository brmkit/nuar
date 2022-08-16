from resources.portscan import *
from resources.netbios import *

class Endpoint:
    '''
        endpoint class definition - nothing more
    '''
    def __init__(self, ip, mac):
        self.ip_address = ip
        self.mac_address = mac
        self.hostname = 'not identified'
        self.ports = 'not defined'
        self.so = 'not defined'

    def print_endpoint(self):
        return {
            "IP": self.ip_address,
            "MAC": self.mac_address,
            "NAME": self.hostname,
            "SO": self.so,
            "PORTS": self.ports
            }
    
    def get_ports(self, ports):
        self.ports = start_scan(self.ip_address,ports)

    def get_os(self):
        self.so = os_guessing(self.ip_address)
    
    def get_hostname(self):
        self.hostname = netbios_name(self.ip_address)

    @staticmethod
    def create_from_dict(dict_endpoints):
        endpoints = []
        for endp in dict_endpoints:
            ip,mac,hstnm,ports,so = endp.values()               
            endpoints.append(Endpoint(ip,mac,hstnm,ports,so))
        return endpoints