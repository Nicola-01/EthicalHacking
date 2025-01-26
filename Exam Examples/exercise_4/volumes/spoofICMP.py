#!/bin/env python3
from scapy.all import IP, TCP, send, ICMP
from ipaddress import IPv4Address
from random import getrandbits

src_addr = "10.9.0.8"
dst_addr = "10.9.0.7"
ip_pk = IP(src = src_addr, dst = dst_addr)
send(ip_pk/ICMP())
