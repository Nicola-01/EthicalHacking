#!/usr/bin/env python3
import argparse
from scapy.all import *

def traceroute(destination_ip):
    for ttl in range(1, 50):

        ip = IP(dst=destination_ip, ttl=ttl)
        icmp = ICMP()

        print(f"Sending packet with TTL={ttl} to {destination_ip}")
        response = sr1(ip/icmp, verbose=False, timeout=2)  # Timeout to avoid waiting too long
        
        if response is None:
            print(f"TTL={ttl}: No response")
            break  # Stop if no response is received
        
        elif response.haslayer(ICMP):
            if response.getlayer(ICMP).type == 0: # Echo Reply
                print(f"TTL={ttl}: Reached destination {destination_ip}")
                break  # Destination reached
            elif response.getlayer(ICMP).type == 11: # Time Exceeded 
                print(f"TTL={ttl}: Hop from {response.src}")
            else:
                print(f"TTL={ttl}: Unexpected ICMP response from {response.src}")
        else:
            print(f"TTL={ttl}: Received non-ICMP response from {response.src}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Perform a traceroute to a specified IP address.')
    parser.add_argument('destination_ip', type=str, help='The destination IP address to trace.')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run traceroute with the provided arguments
    traceroute(args.destination_ip)

if __name__ == "__main__":
    main()