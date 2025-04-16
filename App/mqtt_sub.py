import paho.mqtt.client as mqtt
import ssl
from Send_IR_Request import send_request_ir

CURRENT_IR_STATUS = 0
CURRENT_LIGHT_AIR_STATUS = 0

# AWS IoT endpoint
endpoint = "a3n610pzjgx5l4-ats.iot.ap-southeast-2.amazonaws.com"  # Replace with your IoT endpoint
port = 8883  # Standard port for secure MQTT
topic = "SWBOT/IR"  # Replace with your topic

# Paths to certificates
root_ca_path = "APP/AmazonRootCA1.pem"
cert_path = "APP/SWBOT.pem.crt"
private_key_path = "APP/SWBOT.private.pem.key"

# Devices ID
DEVICES_ID = ["02-202501281947-75389738","02-202501281952-61305966"]
# MQTT client ID
client_id = "my_mqtt_subscriber"  # Unique client ID for your connection


# Callback for MQTT connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic after connecting
    client.subscribe(topic)

# Callback for receiving messages
def on_message(client, userdata, msg):
    global CURRENT_IR_STATUS, CURRENT_LIGHT_AIR_STATUS
    CD = ""
    IR_STATUS = int(msg.payload.decode())
    print(f"IR_STATUS: {IR_STATUS}, CURRENT_IR_STATUS: {CURRENT_IR_STATUS}, CURRENT_LIGHT_AIR_STATUS: {CURRENT_LIGHT_AIR_STATUS}")
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")
    
    if (IR_STATUS == 1) and (IR_STATUS != CURRENT_IR_STATUS):
        if CURRENT_LIGHT_AIR_STATUS == 1:
            
            CURRENT_LIGHT_AIR_STATUS = 0
            CD = "turnOff"
        else:
            CURRENT_LIGHT_AIR_STATUS = 1
            CD = "turnOn"
            
        send_request_ir(CD, DEVICES_ID[1])
        client.publish("SWBOT/LIGHT_AIR", CURRENT_LIGHT_AIR_STATUS)
        print(f"CD: {CD}")
    CURRENT_IR_STATUS = IR_STATUS
    

# Create MQTT client instance
client = mqtt.Client()

# Set up TLS for secure communication
client.tls_set(ca_certs=root_ca_path,
              certfile=cert_path,
              keyfile=private_key_path,
              cert_reqs=ssl.CERT_REQUIRED,
              tls_version=ssl.PROTOCOL_TLSv1_2)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to AWS IoT
client.connect(endpoint, port=8883)

# Start the loop to keep the connection alive
client.loop_start()

# Keep the script running to continuously receive messages
try:
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("Disconnected by user")

# Stop the loop when done
client.loop_stop()
