import json
import pandas as pd
from kafka import KafkaConsumer
from time import sleep



from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem
consumer = KafkaConsumer(
    'TestLaxmi',
     bootstrap_servers=['localhost:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))
# for c in consumer:
#     print(c.value)
s3 = S3FileSystem()
for count, i in enumerate(consumer):
    
    with s3.open("s3://stock-analysis-kafka/source-kafka/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)  
    
    print(i.value)
 


from s3fs import *

consumer = KafkaConsumer('TestLaxmi',
              bootstrap_servers=['localhost:9092'],
                          value_deserializer=lambda x: json.loads(x.decode('utf-8')))

from s3fs import S3FileSystem 
s3 = S3FileSystem()

for c in consumer:
    print(c.value)

import os

os.environ['AWS_ACCESS_KEY_ID'] = 'AKIARSLD6SDI2TPZZZ6I'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

for count, i in enumerate(consumer):
    with s3.open("s3://kafka-stock-market-tutorial-youtube-darshil/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)    

with s3.open("s3://kafka-stock-market-tutorial-youtube-darshil/stock_market_{}.json".format(1), 'w') as file:
        json.dump(consumer, file)  

