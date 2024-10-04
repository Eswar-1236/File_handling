import pymongo 
# mongodb://localhost:27017
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['11am']
user_coll=db['user']
#user_coll.find()#it will find the all data
# user_list=user_coll.find()
# for i in user_list:
#     print(i['id'],i['name'])
#to insert the data(user_list.insert_one(values in the form dictionary))
# user_coll.insert_one({'id':6,'name':'Eswar','gender':'Male'})
# client.close()
# user_coll.update_one({'id':3},{"$set":{"age":200}})


