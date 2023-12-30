#pip install kafka-python

import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json

# it is serializer has  a result we need to send it in particular format 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:json.dumps(x).encode('utf-8')) 

producer.send('TestLaxmi',value='{"name":"Laxmi Priyadarshini"}')

producer.send('TestLaxmi',value='{"name":"Krupa Rani Soma"}')                    

producer.send('TestLaxmi',value='{"name":"hello"}')                    

df = pd.read_csv("indexProcessed.csv")

df.head(5).to_dict(orient="records")[0]

producer.send('TestLaxmi',value=df.head(5).to_dict(orient="records")[0]) 

while True:
    producer.send('TestLaxmi',value=df.head(5).to_dict(orient="records")[0])    
    sleep(1)

while True:
    dict_stock = df.sample().to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    sleep(1)

producer.flush


#pip install kafka-python
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
#producer.send('demo_test', value={'surnasdasdame':'parasdasdmar'})
df = pd.read_csv("indexProcessed.csv")
df.head()
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('TestLaxmi', value=dict_stock)
    sleep(1)
producer.flush() #clear data from kafka server
 
 

