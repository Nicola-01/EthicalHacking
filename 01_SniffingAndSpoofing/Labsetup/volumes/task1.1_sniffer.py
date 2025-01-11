#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt_icmp = sniff(iface='br-d86ec7a3cd9b:', filter='icmp', prn=print_pkt) # Tested with -> ping 1 10.9.0.5 -c

# pkt_filter = sniff(iface='br-973e506c5f0f:', filter='tcp and host 10.9.0.6 and dst port 23', prn=print_pkt) 
# -> Tested with nc 10.9.0.5 23
