import json 
#import requests
import paho.mqtt.client as mqtt
import time
#import ast
from elasticsearch import Elasticsearch

es=Elasticsearch()
false = 0

def json_parser(msg):
    msgList = json.loads(msg.payload.decode())
    sensNum = len(msgList)
    name = sensNum * [None]
    esJson = sensNum * [None]
    esIndex = sensNum * [None]

    for i in range(0, sensNum):
        name[i] = msgList[i]['name']
        dataNum = len(msgList[i]['values'])
        esJson[i] = dataNum * [None]
        esIndex[i] = dataNum * [None]
        dataIndex = {
            'index': {
                "_index" : "es_iot_01",
                "_type" : name[i]
                     }
                    }
        
        for j in range(0, dataNum):
            esJson[i][j] = {
                'sensor': name[i],
                'timestamp': msgList[i]["values"][j]["timestamp"],
                'value' : float(msgList[i]["values"][j]["value"]),
                    }
            #esJson[i][j] = [dataIndex, dataValue]
            #data = json.dumps(data)
            #print(data)
            #esJson[i][j] = '\n'.join(json.dumps(d) for d in data)
            #esJson[i][j] = json.dumps(data)
        dataSend=[dataIndex, esJson[i][0]]
        for j in range(1, dataNum):
            dataSend.append(dataIndex)
            dataSend.append(esJson[i][j])
        es.bulk(body=dataSend)   
                  
    return


#events on connecting, publishing, message etc

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("topic: iot_001")
    client.subscribe("iot_001")

def on_publish(client, userdata, mid):
    print("on publish")

def on_message(client, userdata, msg):
    print("on message at: " +  str(time.time()))
    #print(msg.payload.decode())
    print(msg.topic)

    #important as fuck
    #ajson=json.loads(msg.payload.decode())
    #print(ajson)
    #print(ajson[1])
    #print(ajson[1]["name"])

    data = json_parser(msg)
    # data_to_post = '\n'.join(json.dumps(d) for d in data)
    #es.bulk(body=data)
    



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

