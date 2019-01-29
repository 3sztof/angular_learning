import json 
import requests
import paho.mqtt.client as mqtt
import time
from elasticsearch import Elasticsearch

es=Elasticsearch()


false = "False"
def json_parser(msg):
    msgList = bb#json.loads(json.dumps(msg.payload.decode()))
    print("msgList below")
    print(msgList)
    msgLen=len(msgList)
    for i in range(0, msgLen):
        print("msgList " + str(i) + " below")
        print(msgList[0])
        name[i] = msgList[i]['name']
        print("name " + str(i) + " below")
        print(name[i])
        valLen = len(msgList[i][" values"])
        print("valLen=" + valLen)
    return name

bb=str([{'values': [{'value': 'False', 'timestamp': '2017-08-18T08:31:02.179Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.280Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.382Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.483Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.583Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.687Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.887Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:02.987Z'}, {'value': 'False', 'timestamp': '2017-08-18T08:31:03.089Z'}], 'name': 'Przycisk'}, {'values': [{'value': 5.222929954528809, 'timestamp': '2017-08-18T08:31:02.180Z'}, {'value': 5.1273884773254395, 'timestamp': '2017-08-18T08:31:02.281Z'}, {'value': 5.222929954528809, 'timestamp': '2017-08-18T08:31:02.382Z'}, {'value': 5.350318431854248, 'timestamp': '2017-08-18T08:31:02.483Z'}, {'value': 5.191082954406738, 'timestamp': '2017-08-18T08:31:02.584Z'}, {'value': 5.222929954528809, 'timestamp': '2017-08-18T08:31:02.687Z'}, {'value': 5.03184700012207, 'timestamp': '2017-08-18T08:31:02.887Z'}, {'value': 5.191082954406738, 'timestamp': '2017-08-18T08:31:02.988Z'}, {'value': 5.286624431610107, 'timestamp': '2017-08-18T08:31:03.089Z'}], 'name': 'Analog'}])

print("bb")
print(bb)
print("len(bb)")
print(len(bb))

print("bb[1]")
print(bb[1])

print("bb[1][name]")
print(bb[1]["name"])

def json_parser(msg):
    msgList = bb#json.loads(json.dumps(msg.payload.decode()))
    print("msgList below")
    print(msgList)
    msgLen=len(msgList)
    for i in range(0, msgLen):
        print("msgList " + str(i) + " below")
        print(msgList[0])
        name[i] = msgList[i]['name']
        print("name " + str(i) + " below")
        print(name[i])
        valLen = len(msgList[i][" values"])
        print("valLen=" + valLen)
    return name

