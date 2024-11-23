from scapy.all import *  # Import all functions and classes from the Scapy library

# Prompt the user to enter a destination IP address
destination_ip = input("Enter the destination IP address (default is '8.8.8.8'): ") or "8.8.8.8"

# Create an IP packet with the specified destination IP address
packet = IP(dst=destination_ip) / ICMP()  # Create an ICMP packet (ping)

# Send the packet
send(packet)  # Send the crafted packet to the destination