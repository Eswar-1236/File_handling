import csv
import pymongo
import json
import requests
db=requests.get("https://jsonplaceholder.typicode.com/users")
collect=db.json()
# fp=open("rocky.json",'w+')
# a=json.dumps(collect)
# fp.write(a)
fp1=open("rocky.csv","w+",newline="")
k=csv.writer(fp1)
k.writerow(collect[0].keys())
[k.writerow(i.values()) for i in collect]
# m=len(collect)
# m1=0
# while m1<m:
#     k.writerow(collect[m1].values())
#     m1+=1


    
