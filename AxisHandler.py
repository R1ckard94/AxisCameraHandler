from multiprocessing.connection import Client
import paho.mqtt.client as mqtt
import  json, time


def sendToApi(jsonMsg): #det som sållas fram av "isValid"
    print()

def isValid(jsonMsg):
    #behöver ingen kö för att även om mitt program är segt så kommer brokern skicka ut det som kommer fram till den ändå
    if(jsonMsg["class"] == 'Person'):
        #print("diz is person")
        tmp = jsonMsg["path"]
        tmpArr = []
        for tm in tmp:
            tmpArr.append(tm["x"])
        #print(tmpArr)
        if(tmpArr[0] < tmpArr[-1]): #går från vänster till höger 
            if(tmpArr[-1] > 250): #måste nog ändra så att storleken blir mindre eller större beroende på data som kommer in
                 print("en person har gått ut!")
                 return
        if(tmpArr[0] > tmpArr[-1]):
            if(tmpArr[0] < 250):
                print("en person har gått in!")
                return

    if(jsonMsg["class"] == 'Vehicle'):
        print("diz is Vehicle")
        


def on_connect(client, userdata, flags, rc):
    if(rc != 0):
        print("Connection code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    #print(msg.topic+" :: "+str(msg.payload)) #får konstigt " b'payload' "
    #print("thread activitiy")
    isValid(json.loads(msg.payload))
    time.sleep(4)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "user123")
client.connect("localhost", 1883, 60)
client.loop_forever()