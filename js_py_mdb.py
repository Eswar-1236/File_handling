import pymongo
import json
client=pymongo.MongoClient("mongodb://localhost:27017/")
# data=open("users.json",'r')
# client.drop_database('11am')
# print("the dtata base is successfully droped")
db_in_client=client['12am']
user=db_in_client['data']
# list=json.load(data)
# user.insert_many(list)
# a=user.find()
# for i in a:
#     print(i)
quer={'id':1}
user.delete_many(quer)

