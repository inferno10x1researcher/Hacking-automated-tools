import shodan  # Import the Shodan library for API access

# Prompt the user to enter their Shodan API key
SHODAN_API_KEY = input("Enter your Shodan API key: ")

# Initialize the Shodan API client with the provided API key
api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Query the Shodan API for information about the specified host (8.8.8.8)
    result = api.host('8.8.8.8')
    
    # Print the result returned by the API
    print(result)
except shodan.APIError as e:
    # Handle any API errors that occur and print the error message
    print('Error: {}'.format(e))