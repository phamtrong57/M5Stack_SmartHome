import requests
from GenerateHeader import generate_header

def send_request_ir(CD, DEVICE_ID):
    # Prepare the command
    # CD = "turnOn"
    command = {
        "command": CD,  # Change to "turnOff" to turn off
        "parameter": "default",
        "commandType": "command"
    }

    headers = generate_header()
    # DEVICE_ID = "02-202501281952-61305966"
    # Send the request
    url = f"https://api.switch-bot.com/v1.1/devices/{DEVICE_ID}/commands"
    response = requests.post(url, json=command, headers=headers)

    # Check the response
    if response.status_code == 200:
        print("Command sent successfully!")
        print(response.json())
        return response.json
    else:
        print("Failed to send command.")
        print(response.status_code, response.text)
        return response.status_code

