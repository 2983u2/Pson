import requests
from Pson import *

# Set the URL of the website you want to send the request to
url = "https://example.com/api/endpoint"

# Set the data you want to send in the request body
data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Convert the data to Pson format
pson_data = JParse(str(data))

# Set the headers for the request
headers = {
    "Content-Type": "application/psongz"
}

# Send the POST request
response = requests.post(url, headers=headers, data=pson_data)

# Check the response status code
if response.status_code == 200:
    print("Request sent successfully!")
    print("Response:", response.text)
else:
    print("Error sending request:", response.status_code)