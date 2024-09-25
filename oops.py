#class is template,used to create an object
#class contains variables and methods
# class Employee:
#     loc_id=101
# e1=Employee()
# e2=Employee()
# print(e1)
# print(e2)
# print(id(e1))
# print(id(e2))
# print(e1.__dict__)
# print(e2.__dict__)
# print(Employee.__dict__)
class Employe:
    min_bal=100
    #instance--:self means instance method
    #selef is a pointer ponting to current object
    def open_ac(self):
        print("ac open succes")
    #class method
    @classmethod
    def m2(cls):
        pass
    #static method
    @staticmethod
    def m3():
        pass
a1=Employe()
a2=Employe()
a3=Employe()
#how to print class numbers
print(a1.__dict__)
print(a2.__dict__)
print(Employe.__dict__)

