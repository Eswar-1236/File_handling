import pandas as pd
a=pd.read_csv("dummy.csv")
print(a['firstName'][:2])#we can do slicing operation
print(a.iloc[0])#we canselect he first row of data in the data frame
print(a.iloc[:3,[1,2]])#a.iloc[start value:stop value,row number or list of row nums[1,2]]
print(a.iloc[-5:])
print(a.loc[:,['id','firstName','age','bloodGroup']])


