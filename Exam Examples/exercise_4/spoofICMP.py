#!/bin/env python3
from scapy.all import IP, TCP, send, ICMP
from ipaddress import IPv4Address
from random import getrandbits

src_addr = "***"
dst_addr = "***"
ip_pk = IP(src = src_addr, dst = dst_addr)
send(ip_pk/ICMP())
