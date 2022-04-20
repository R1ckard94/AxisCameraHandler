from multiprocessing.connection import Client
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("#")

def on_message(client, userdata, msg):
    print(msg.topic+" :: "+str(msg.payload)) #får konstigt " b'payload' "

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "user123")
client.connect("localhost", 1883, 60)

client.loop_forever()