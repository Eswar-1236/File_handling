import pandas as pd
a=pd.read_csv("dummy.csv")
b=pd.read_csv("bbb.csv")
# print(a['firstName'][:2])#we can do slicing operation
# print(a.iloc[0])#we canselect he first row of data in the data frame
# print(a.iloc[:3,[1,2]])#a.iloc[start value:stop value,row number or list of row nums[1,2]]
# print(a.iloc[-5:])
# print(a.loc[:,['id','firstName','age','bloodGroup']])
# p=a.rename(columns={'firstName':'Name'})
# print(p.iloc[:5,[1,2,3,4,5]])
# p1=a.rename(columns={'lastName':'Lname','firstName':'Name'})
# print(p1.iloc[:5,[1,2,3,4,5,6]])
m=a['firstName']
m1=b['name']
print(pd.concat([m,m1]))






