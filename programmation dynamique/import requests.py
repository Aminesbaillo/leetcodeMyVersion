import requests

# Define the API endpoint
url = 'https://headers.scrapeops.io/v1/user-agents'

# Specify the API key
api_key = '9a73dc5a-bcc1-4d98-bd28-f1665810e9e9'

# Send a GET request to the API endpoint with the API key as a query parameter
response = requests.get(url, params={'api_key': api_key})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response body which contains the user agents list
    print('User Agents List:', response.json())
else:
    # Print an error message if the request was not successful
    print('Error:', response.text)
