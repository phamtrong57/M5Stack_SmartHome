import json
import os
from GenerateHeader import generate_header
import requests

# API endpoint
url = "https://api.switch-bot.com/v1.1/devices"

# Header for GET request
headers = generate_header()

# Make the Get Request
response = requests.get(url, headers=headers)

#Check the response
if response.status_code == 200:
    devices = response.json()
    with open ("App/Response/GET_Devices.json","w") as file:
        json.dump(devices, file, indent=4)
else:
    print(f"Error: {response.status_code}")
    print("Response:", response.text)

