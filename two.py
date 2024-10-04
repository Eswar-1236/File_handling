import json
import requests
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['12am']
user_collection=db['data']
a=requests.get("https://jsonplaceholder.typicode.com/users")
list=a.json()
# print(type(list))
ls1=[]
for i in list:
    ls1.append({"id":i['id'],"name":i['name'],"username":i['username'],"address":i['address']['city']})
# print(ls1)
user_collection.insert_many(ls1)
client.close()
