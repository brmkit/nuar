import sys
import socket
from scapy.all import ARP, Ether, srp, ICMP, sr1, IP
from concurrent.futures import ThreadPoolExecutor, thread

def os_guessing(ip):
    #   ------------- TO DO -------------
    # define a better os_guessing function
    print(f'os guessing: {ip}')
    icmp_packet = sr1(IP(dst=ip)/ICMP(), timeout=3, verbose=False)
    if icmp_packet == None:
        return
    if icmp_packet.ttl == 64:
        return 'Unix System'
    elif icmp_packet.ttl == 128:
        return 'Windows System'
    elif icmp_packet.ttl == 255:
        return 'Cisco System'
    else:
        return 'Undefined'

def portscan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    res = s.connect_ex((ip, port))
    if res == 0:
        s.close()
        return port
    else:
        s.close()

def start_scan(ip, ports):

    print(f'portscan: {ip}')
    processes = []

    with ThreadPoolExecutor(max_workers=3) as POOL:
        try:
            for port in ports:
                processes.append(POOL.submit(portscan, ip, port))
        except KeyboardInterrupt:
            POOL._threads.clear()
            thread._threads_queues.clear()
            sys.exit('\n******* closing threads *******')

    return [proc.result() for proc in processes if proc.result() != None]