from storm import Spout, emit, log
import time
import datetime
from random import randrange
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka import KafkaClient
from kafka import SimpleConsumer
import json
client = KafkaClient("ip-172-31-88-122.ec2.internal:6667")
consumer = SimpleConsumer(client, "test-group", "forestfire")

def getData():
    data = consumer.get_messages(count = 1, block=True,timeout=0.1)	
    try: 
        return data[0][1].value
    except:
	return "empty"
	
class MySpout(Spout):
    def nextTuple(self):
        data = getData()
        if (data!= "empty"):
            emit([data])
   
MySpout().run()
