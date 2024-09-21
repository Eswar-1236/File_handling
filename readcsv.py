import csv
fp=open('emp.csv','r')
rows=csv.reader(fp)
user=list(rows)
for i in user[1:]:
    print(i)