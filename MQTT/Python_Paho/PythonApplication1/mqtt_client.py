######### Sending msg via mqtt and collecting it in elasticsearch ############
# libraries:
# json - for sendng json's files to elastic
# request for http request and communication with elastic
# paho.mqtt.client for using mqtt with python
# time for sending timestamp in test msg ( not essential )
#
#
import json 
import requests
import paho.mqtt.client as mqtt
import time
from elasticsearch import Elasticsearch

#initialization of elasticsearch
es=Elasticsearch()

false = 0

#function for sending from mqtt to es
def json_sender(msg):
    msgList = json.loads(msg.payload.decode())
    #checking no of sensors
    sensNum = len(msgList)

    name = sensNum * [None]
    esJson = sensNum * [None]
    esIndex = sensNum * [None]

    for i in range(0, sensNum):
        #name of sensor
        name[i] = msgList[i]['name']
        #no of data
        dataNum = len(msgList[i]['values'])

        esJson[i] = dataNum * [None]
        esIndex[i] = dataNum * [None]
        #header for _bulk
        dataIndex = {
            'index': {
                "_index" : "es_iot_01",
                "_type" : name[i]
                     }
                    }
        #reading values from mqtt
        for j in range(0, dataNum):
            esJson[i][j] = {
                'sensor': name[i],
                'timestamp': msgList[i]["values"][j]["timestamp"],
                'value' : float(msgList[i]["values"][j]["value"]),
                    }
        #creating list for sending
        dataSend=[dataIndex, esJson[i][0]]
        for j in range(1, dataNum):
            dataSend.append(dataIndex)
            dataSend.append(esJson[i][j])
        #sending
        es.bulk(body=dataSend)   
                  
    return

#events on connecting, publishing, message etc
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("iot_001")

def on_publish(client, userdata, mid):
    print("on publish")

def on_message(client, userdata, msg):
    print("on message at: " +  str(time.time()))
    print(msg.topic)
    json_sender(msg)


#creating object client for mqtt
client = mqtt.Client(client_id="IoTClient01", userdata="VSTest")


#assing events
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

#login and connect to mqtt broker
client.connect("localhost", 1883)

#loop for staing connected with mqtt broker
client.loop_forever()

