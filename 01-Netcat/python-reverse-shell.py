import socket

def create_connection(host, port):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server's address and port
    s.connect((host, port))
    
    # Continuously receive data from the server
    while True:
        # Receive up to 1024 bytes of data from the socket
        data = s.recv(1024)
        
        # Check if any data was received
        if data:
            # Decode the received bytes and print the result
            print(data.decode())
        
        # Send user input to the server
        s.send(input("Shell> ").encode())
    
    # Close the socket (this line will never be reached due to the infinite loop)
    s.close()

# Get user input for the IP address and port
host = input("Enter the server IP address (default '127.0.0.1'): ") or '127.0.0.1'
port = input("Enter the server port number (default '12345'): ") or '12345'

# Convert port input to an integer
port = int(port)

# Create a connection to the specified server
create_connection(host, port)