import subprocess

# Get user input for the target URL
target_url = input("Enter the target URL for Nikto scan (default is 'http://example.com'): ") or 'http://example.com'

# Run the Nikto command with the specified target URL
subprocess.run(['nikto', '-h', target_url])