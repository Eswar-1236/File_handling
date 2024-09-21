import json
import csv
customer=[
    {'id':101,'name':'eswar','avail':False},
    {'id':102,'name':'shiva','avail':True},
    {'id':103,'name':'shanu','avail':False}
]
# fp=open('emp.json','w+')
fp1=open('emp.csv','w+',newline="")
# json.dump(customer,fp)
a=csv.writer(fp1)
a.writerow(['id','name','avail'])
for i in customer:
    a.writerow([i['id'],i['name'],i['avail']])
# fp.write(a)
# fp.close()
fp1.close()