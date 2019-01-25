import paho.mqtt.client as mqtt
import time
import json
import pandas as pd
import numpy
import random
from collections import deque


#df = pd.DataFrame({'time': [1], 'temperature': [1]})
#df2 = pd.DataFrame({'time': [1], 'temperature': [2012]})
#df2 = pd.DataFrame([["5", "6"]], columns = ['time','temperature'])
#df = df.append(df2)
#df.set_index('time', inplace = True)
#print(df)
#df.to_csv('aqua.csv', mode='a', header=False)

#X = deque(maxlen=20)
#X.append(1)
#MQTT Details
broker_address="iot.eclipse.org"
client_id="autobot_sub"
sub_topic="greenhouse/temp"
pub_topic="greenhouse/temp"

try:
#pandas reas csv file
	df = pd.read_csv("aqua.csv")
        print(df)
except:
	print("error reading csv file, creating dataframe")
        df_create = pd.DataFrame([["2018-12-22 01:22:29", "1"]], columns = ['time','temperature'])
	df_create.to_csv('aqua.csv', mode='a', header=True)
	#df = pd.read_csv("aqua.csv")

#Callback function on message receive
def on_message(client,userdata,message):
      
       print("message received",str(message.payload.decode("utf-8")))
       data = json.loads(str(message.payload.decode("utf-8","ignore")))
       print(data)
       #X.append(X[-1]+1)
       #df2 = pd.DataFrame([[X[-1], data[1]]])
       df2 = pd.DataFrame([data])
       df2.to_csv('aqua.csv', mode='a', header=False)
       print("message topic=",message.topic)
       print("message qos=",message.qos)
       print("message retain flag=", message.retain)


#callback function on log
def on_log(client, userdata, level,buf):
       print("log: ", buf)

#MQTT init
print("Initalizing MQTT Client instance: " + client_id)
client =  mqtt.Client(client_id)

#Bind function to callback
client.on_message = on_message
client.on_log = on_log

#Connect to broker
print("connecting to broker: " + broker_address)
client.connect(broker_address)
try:
    client.loop_start()
    print("subscribing to topic " + sub_topic)
    client.subscribe(sub_topic)
    while True:
          print("waiting")
	  time.sleep(100)

except:
    print("error")
    client.loop_stop()

