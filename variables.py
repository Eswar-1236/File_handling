# class test:
#     def __init__(self,id) -> None:
#         self.id=id
#     def m1(self):
#         self.name="eswar"
    # @classmethod
    # def m2(self,sal):
    #     self.sal=sal
    # @staticmethod
    # def m3():
    #     return 'tcs'
# a=test(100)
# a.m1()
# print(a.__dict__)
# a2=test(101)
# a2.m1()
# print(a2.__dict__)

# print(a.m1('eswar'))
# print(a.m2(3333))
# print(a.m3())


# how to create static variable,inside class-->out side method,inside class -->using class name,out-side class--->using class name
class test2:
    a=100
    def __init__(self) -> None:
        test2.b=100
    def m(self):
        test2.a1=200
    @classmethod
    def m1(cls):
        test2.c=300
        cls.d=400
    @staticmethod
    def m2():
        test2.e=500
b=test2()
b.m()
b.m1()
b.m2()
print(test2.__dict__)