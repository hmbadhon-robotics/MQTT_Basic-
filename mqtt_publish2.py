import paho.mqtt.client as mqtt

from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker)

while True:
    randNumber = randrange(15)
    client.publish("Temperature", randNumber)
    print("Just published " + str(randNumber) + " to topic temperature ")
    time.sleep(1)
