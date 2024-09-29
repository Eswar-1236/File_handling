class Employe:
    company='Tcs'
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
a=Employe(101,'Eswar',32323)
a1=Employe(102,'shiva',32323)
a2=Employe(103,'shanu',32323)
print(a.__dict__)
print(a1.__dict__)
print(a2.__dict__)
# print(Employe.__dict__)


