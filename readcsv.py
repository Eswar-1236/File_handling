import csv
import json
fp=open('dummy.csv','r')
rows=csv.reader(fp)
user=list(rows)
fp1=open('rrr.json','w+')
c=list(user[0])
dict={}
m=0
for i in user[1:]:
    for x in i:
        if m<len(user):
            dict[c[m]]=x
            m+=1
    fp1.write(json.dumps(dict))    
    m=0



# b=["ew","ww","Wr"]
# a=[10,20,30]
# dict={}
# for i in range(len(a)):
#     dict[a[i]]=b[i]
#     # print(c)
# print(dict)




