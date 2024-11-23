import nmap

# Create an instance of the PortScanner
nm = nmap.PortScanner()

# Get user input for the target IP address
target_ip = input("Enter the target IP address (default '127.0.0.1'): ") or '127.0.0.1'

# Get user input for the port range
port_range = input("Enter the port range to scan (default '22-1024'): ") or '22-1024'

# Perform the scan on the specified IP and port range
nm.scan(target_ip, port_range)

# Print all hosts found during the scan
print("All hosts found:")
print(nm.all_hosts())