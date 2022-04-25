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
    #behöver ingen kö för att även om mitt program är segt så kommer brokern skicka ut det som kommer fram till den ändå
    if(jsonMsg["class"] == 'Person'):
        tmp = jsonMsg["path"]
        tmpArr = []
        for tm in tmp:
            tmpArr.append(tm["x"])
            
        if(tmpArr[0] < tmpArr[-1]): #går från vänster till höger 
            if(tmpArr[-1] > 250): #måste nog ändra så att storleken blir mindre eller större beroende på data som kommer in
                print("person in")
                sendToApi(True)
                return
        if(tmpArr[0] > tmpArr[-1]): #går från höger till vänster
            if(tmpArr[-1] < 250):
                print("person ut")
                sendToApi(False)
                return

    #if(jsonMsg["class"] == 'Vehicle'): test case för att se om vehicle funkar, men behövs inte
        #print("diz is Vehicle")
        


def on_connect(client, userdata, flags, rc):
    print("Connection code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    #print(msg.topic+" :: "+str(msg.payload)) 
    isValid(json.loads(msg.payload))
    time.sleep(4)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "user123")
client.connect("localhost", 1883, 60)
client.loop_forever()