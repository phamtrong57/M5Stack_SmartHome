import paho.mqtt.client as mqtt
import ssl
import time

# AWS IoT endpoint
endpoint = "a3n610pzjgx5l4-ats.iot.ap-southeast-2.amazonaws.com"  # Replace with your IoT endpoint
port = 8883  # Standard port for secure MQTT
topic = "SWBOT/ORDERS"  # Replace with your topic

# Paths to certificates
root_ca_path = "AmazonRootCA1.pem"
cert_path = "SWBOT.pem.crt"
private_key_path = "SWBOT.private.pem.key"

# MQTT client ID
client_id = "my_mqtt_publisher"  # Unique client ID for your connection

# Callback for MQTT connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Create MQTT client instance
client = mqtt.Client()

# Set up TLS for secure communication
client.tls_set(ca_certs=root_ca_path,
              certfile=cert_path,
              keyfile=private_key_path,
              cert_reqs=ssl.CERT_REQUIRED,
              tls_version=ssl.PROTOCOL_TLSv1_2)

# Set the callback function for connection
client.on_connect = on_connect

# Connect to AWS IoT
client.connect(endpoint, port=8883)

# Start the loop to keep the connection alive
client.loop_start()

# Continuous loop to publish messages every 5 seconds
try:
    while True:
        message = "Hello from my publisher!"
        client.publish(topic, message)
        print(f"TOPIC: {topic}")
        print(f"Message published: {message}")
        time.sleep(5)  # Publish every 5 seconds (adjust as needed)
except KeyboardInterrupt:
    print("Disconnected by user")

# Stop the loop when done (no subscription or listening needed)
client.loop_stop()
