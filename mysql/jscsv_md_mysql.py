import json
import csv
import pymongo
import requests
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['csv']
collector=db['data']
fp=open("rocky.csv")
obj=csv.reader(fp)
colect=list(obj)
a=colect[0]
l=[]
for i in colect[1:]:
    dict={}
    for x in range(len(i)):
        dict[a[x]]=i[x]
    l.append(dict)
collector.insert_many(l)
db1=client['json']
collector1=db1['json_data']
fp=open("rocky.json")
list=json.load(fp)
collector1.insert_many(list)


