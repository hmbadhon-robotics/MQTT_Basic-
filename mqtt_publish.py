import paho.mqtt.client as mqtt

from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0,25.0)
    client.publish("Temperature", randNumber)
    print("Just published " + str(randNumber) + " to topic temperature ")
    time.sleep(1)
