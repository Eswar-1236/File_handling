import pymongo
from emp import l
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['11am']
user_coll=db['user']
l=user_coll.find()
# for i in l:
# user_coll.insert_many(l)
m={'id':121,'name':"ANATPUR",'gender':"State"}
for i in l:
    if i['id']==4:
        user_coll.update_one(update=m)
    else:
        continue
client.close()

