import csv
import ipaddress
import random
from time import sleep
from random import randint
from resources.fileint import *
from resources.endpoint import Endpoint
from scapy.all import ARP, Ether, srp, ICMP, sr1, IP
    
def define_sleep(method,i):
    '''
    placeholder function - in future implementation can be used as sleep generator for each packet
    for a stealthier life
    '''
    sleep(random.randint(15,60))

def do_arp(target_ip, interface):
    '''
    create arp packet, send it and move on.
    '''
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip) 
    result = srp(packet, timeout=1, iface=interface, verbose=0)[0]                
    for _, recv in result:
        return recv.psrc,recv.hwsrc                                                  # receive ip and mac-address

def do_recon(subnet_ip, interface, paranoid=None, endp_file = None):
    '''
    perform recon using a single arp packet for each ip
    prevents arp-storm and allows more control over packet flow
    '''
    ENDPOINTS = []

    if endp_file:
        dict_endpoints = load_csv(endp_file)                                          # load alredy seen endpoints - if needed  
        ENDPOINTS = Endpoint.create_from_dict(dict_endpoints)
    
    range_ip = [ip.compressed for ip in ipaddress.ip_network(subnet_ip)]              # range generator

    for n, ip in enumerate(range_ip):
        if paranoid:
            define_sleep()                                                            # maybe a stealth function?
        #print(f"start with {ip}")
        if ip in [endpoint.ip_address for endpoint in ENDPOINTS]:
            continue
        try:
            ip, mac = do_arp(ip, interface)                                          # unpack generates error when no one responds
        except:
            continue
        print(f"response {ip} - {mac}")
        ENDPOINTS.append(Endpoint(ip,mac))                                           # add endpoint in the object_list
    return ENDPOINTS
