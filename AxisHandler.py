from multiprocessing.connection import Client
from datetime import date, datetime
import paho.mqtt.client as mqtt
import  json, time, requests

url = 'https://peoplecounterapi.azurewebsites.net/api/Counted'

def sendToApi(payload): #det som sållas fram av "isValid"
    dt = datetime.now()
    jsonStr = {
        "date_and_time": str(dt),
        "personIn": payload
    }
    postResult = requests.post(url, json = jsonStr) #omvanldar string till json 
    print(postResult)

def isValid(jsonMsg):
    #programmets data hanterar allt i en kö så att programmet inte blir överflödigt
    tmp = jsonMsg["path"]
    tmpArr = []
    for tm in tmp:
        tmpArr.append(tm["x"])

    if(tmpArr[0] < tmpArr[-1]): #går från vänster till höger 
        if tmpArr[-1] > 450 and tmpArr[0] < 450:  
            print("person in")
            sendToApi(True)
    elif(tmpArr[0] > tmpArr[-1]): #går från höger till vänster
        if tmpArr[0] > 450 and tmpArr[-1] < 450:
            print("person ut")
            sendToApi(False)

        
def on_connect(client, userdata, flags, rc):
    print("Connection code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    if(str(msg.topic) == "xmotion/path/B8A44F0AFAC4"): 
        isValid(json.loads(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "user123")
client.connect("10.1.20.99", 1883, 60)
client.loop_forever()
