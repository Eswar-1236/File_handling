import json
a=open('js.py','r')
emp=json.load(a)
s=open('male.py','w+')
male=list(filter(lambda x:x['gender']==
                 'Male',emp))
json.dump(male,s)
l=open('female.py','w+')
female=list(filter(lambda x:x['gender']=='Female',emp))
json.dump(female,l)
# s.write(str(list(filter(lambda x:x['gender']=='Male',emp))))
# l.write(str(list(filter(lambda x:x['gender']=='Female',emp))))

# print(m)
# a.close()