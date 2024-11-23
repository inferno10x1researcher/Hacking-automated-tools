from scapy.all import sniff

def packet_callback(packet):
    # This function is called for each captured packet
    print(packet.summary())  # Print a summary of the packet

# Get user input for the number of packets to capture
num_packets = input("Enter the number of packets to capture (default is 10): ")

# Use the default value if the user does not provide input
if not num_packets.isdigit():
    num_packets = 10  # Default to 10 packets if input is not a valid number
else:
    num_packets = int(num_packets)  # Convert input to an integer

# Get user input for the protocol or port to filter packets
filter_input = input("Enter the protocol (e.g., tcp, udp) or port (e.g., 80) to filter packets (leave blank for no filter): ")

# Start sniffing packets with the specified filter
if filter_input:
    # If the user provided a filter, use it to filter packets
    sniff(prn=packet_callback, count=num_packets, filter=filter_input)
else:
    # If no filter is provided, capture all packets
    sniff(prn=packet_callback, count=num_packets)