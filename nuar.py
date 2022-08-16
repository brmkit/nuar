import os
import re
import sys
import argparse
from resources.banner import banner
from resources.fileint import *
from resources.endpoint import *
from resources.engine import *

def arguments():
    parser = argparse.ArgumentParser(description='A simple-network-recon tool that enumerates endpoints and define open-ports, for now.')
    parser.add_argument(
        '-n', '--network', required=True, type=str, help='choose a network in IP/MASK format')
    parser.add_argument(
        '-i', '--interface', required=True, type=str, help='interface used for network recon')
    parser.add_argument(
        '-o', '--output', required=True, type=str, help='define an output name file')
    parser.add_argument(
        '-p', '--portscan', metavar='portlist',required=False, type=str, help='define a port list to perform scan ex: 53,88,80,8080')
    parser.add_argument(
        '-name', '--hostname', action='store_true', default=False, help='allow hostname detection [only win*]')
    parser.add_argument(
        '-os','--os-guessing', action='store_true', default=False, help='try to guess remote operating system')
    parser.add_argument(
        '-pnd', '--paranoid', action='store_true', required=False, help='use a random sleeping time for each packet sent')
    parser.add_argument(
        '-in', '--input', required=False, type=str, metavar='input_file', help='import a csv file in nuar.py format')
    
    args = parser.parse_args()
    return args,parser

if __name__ == "__main__":

    '''if os.geteuid() != 0:
        print("root required...")
        exit(-1)'''

    banner()
    args, parser = arguments()
    print(args)

    if not re.search('(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?',args.network):                         # input check...
        print(f'{args.network} not IP/MASK format')
        parser.print_usage(sys.stderr)
        exit(-1)

    if args.input:
        ENDPOINTS = do_recon(args.network,args.interface,args.paranoid,args.input)
    else:
        ENDPOINTS = do_recon(args.network, args.interface, args.paranoid)

    if args.hostname:
        for endp in ENDPOINTS:
            endp.get_hostname()

    if args.portscan:
        ports = [int(port) for port in args.portscan.split(',')]
        for endp in ENDPOINTS:
            endp.get_ports(ports)
    
    if args.os_guessing:
        for endp in ENDPOINTS:
            endp.get_os()
        
    DICT_ENDPOINTS = [endp.print_endp() for endp in ENDPOINTS]

    if args.output:
        extract_csv(DICT_ENDPOINTS, args.output+'.csv')
