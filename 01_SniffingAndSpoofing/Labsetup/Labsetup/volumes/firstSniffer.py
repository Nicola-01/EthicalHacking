#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-e92ebd21a220:', filter='icmp', prn=print_pkt)