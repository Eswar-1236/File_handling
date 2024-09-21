import json
# a=open('users.json','r')
# s=open('jsv.py','w')
# m=json.load(a)
# l=[]
# for i in m:
#     s.write(str(("id's",i["id"],"name's",i["name"],"email's",i["email"])))
# s.write(str(l))
# import json
# a=open('jsv.py','w')
# s=open('one.py','r')
# a.write(str(json.load(s)))
# s.write(m)
l=[]
from file1 import a
import pandas as pd
# c=open('beauty.py','w+')
# for i in a['products']:
#     if i['category']=='beauty':
#         l.append(i)
# c.write(str(l))
m=pd.DataFrame(a)
# a=[i for i in m['products'] if i['category']=='beauty']
# print(a)
# print(z)
print(m)