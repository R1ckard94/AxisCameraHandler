from multiprocessing.connection import Client
import paho.mqtt.client as mqtt
import  json, time




def sendToApi(jsonMsg):
    print()

def isValid(msg):
    #behöver ingen kö för att även om mitt program är segt så kommer brokern skicka ut det som kommer fram till den ändå
    print()
    

def on_connect(client, userdata, flags, rc):
    if(rc != 0):
        print("Connection code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    #print(msg.topic+" :: "+str(msg.payload)) #får konstigt " b'payload' "
    print("thread activitiy")
    #handlingQueue.put(str(msg.payload))
    time.sleep(4)
    print(msg.topic+" :: "+str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "user123")
client.connect("localhost", 1883, 60)
client.loop_forever()
