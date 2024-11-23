import requests

# Get user input for the URL to send the POST request to
url = input("Enter the URL for the login (default is 'http://example.com/login'): ") or 'http://example.com/login'

# Get user input for the username
username = input("Enter the username (default is 'admin'): ") or 'admin'

# Get user input for the password
password = input("Enter the password (default is 'admin'): ") or 'admin'

# Prepare the data for the POST request
data = {'username': username, 'password': password}

# Send the POST request
response = requests.post(url, data=data)

# Print the response text from the server
print("Response from the server:")
print(response.text)