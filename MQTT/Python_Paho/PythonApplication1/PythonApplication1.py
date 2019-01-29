import paho.mqtt.client as paho
import time

#create variable time for testing
time_a=time.time()


# Create mqtt clien
mqttc = paho.Client()

# Connect to broker
mqttc.connect('localhost',1883)

# Start subscribe, with QoS level 0
mqttc.subscribe("hello/world", 0)

# Publish a message
mqttc.publish("hello/world", str(time_a))
