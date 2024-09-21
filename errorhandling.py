# a=int(input("enter ur num :"))
# b=int(input("enter ur num :"))
# print(a/b)
# try:
#     a=int(input("enter ur num :"))
#     b=int(input("enter ur num :"))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("can not divide by zero")
# except ValueError as e:
#     print("can not convert string to int")
# print("welcome")


import requests
import json
import csv
import pandas as pd
# a=requests.get('https://jsonplaceholder.typicode.com/users')
# user=a.json()
# print(user)
api_url='https://jsonplaceholder.typicode.com/users'
user_data=None
try:
    user_data=requests.get(api_url)
    users=user_data.json()
    user_data.raise_for_status()
    fp1=open('aaa.csv','w+',newline="")
    p=csv.writer(fp1)
    for i in users:
        p.writerow(i.keys())
        break
    for i in users:
        p.writerow(i.values())
    print("please check the data in aaa.csv")
except requests.exceptions.RequestException as e:
    fp=open('users.json','r')
    c=json.load(fp)
    fp1=open('bbb.csv','w',newline="")
    p=csv.writer(fp1)
    for i in c:
        p.writerow(i.keys())
        break
    for i in c:
        p.writerow(i.values())
    print("please check the data in bbb.csv file")

finally:
    print("the king of conding")


