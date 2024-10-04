"""collecting the data from api and filter the data and inserting the data into mongodb"""
import requests
import json
import pymongo
user=requests.get("https://jsonplaceholder.typicode.com/users")
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['13am']
user_col=db['ESWAR']
data=user.json()
print(data)
user_list=[]
for i in data:
    user_list.append({'id':i['id'],'user_name':i['username'],'city':i['address']['city'],'website':i['website']})
print(user_list)
# user_col.insert_many(user_list)
# client.close()
