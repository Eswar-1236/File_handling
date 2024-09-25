# class Test:
#     def __init__(self) -> None:
#         print("test_class ---cm")
#     def m1(self):
#         print("test-class --instance method")
#     @classmethod
#     def m2(cls):
#         print("test-class --class method")
#     @staticmethod
#     def m3():
#         print("test calss ---static method")
# a=Test()
# a.m1()
# a.m2()
# a.m3()
# a1=Test()

class Accont:
    "account holder details"
    #static valriable only one copy is created and shared to all objects
    min_bal=2000
    def __init__(self,id,name,ac_bal) -> None:
        # print("account class---constructor method")
        self.id=id
        self.name=name
        self.ac_bal=ac_bal
    def deposit_amount(self,amount):
        # print("account class --instance method")
        # print(amount)
        self.ac_bal=self.ac_bal+amount
m=Accont(101,'rahul',5000)
# m.deposit_amount(8888)
m1=Accont(102,'prahulla',8000)
m2=Accont(103,'priyanka',7000)
m.deposit_amount(1000)
m.deposit_amount(1000)
m1.deposit_amount(100)
m2.deposit_amount(99)
# print(m.min_bal)
print(m.__dict__)
print(m1.__dict__)
print(m2.__dict__)
print(Accont.__dict__)
print(Accont.__doc__)



