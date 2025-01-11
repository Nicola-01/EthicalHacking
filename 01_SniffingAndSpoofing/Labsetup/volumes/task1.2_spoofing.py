#!/usr/bin/env python3
from scapy.all import *

ip = IP()
ip.src = '10.9.0.6' # arbitrary source IP address
ip.dst = '10.9.0.5'
# ip.show()
# You have to create one layer at the time and stack them using the / operator
icmp = ip/ICMP()
# ls(icmp)
send(icmp) # send instand of sendp
# sendp -> you need to specify Layer 2