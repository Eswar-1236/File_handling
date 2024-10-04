import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
# db=client["12am"]
# colection=db['data']
# ls=colection.find()
# for i in ls:
#     print(i['name'])
db=client["11am"]
colection=db['user']
query={'id':10}
colection.delete_one(query)
print(colection)