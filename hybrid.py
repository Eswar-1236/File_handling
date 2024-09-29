class Gp1:
    def m1(self):
        print("grand parent class m1")
class p1(Gp1):
    def m2(self):
        print("parent p1 class m2")
class p2(Gp1):
    def m3(slef):
        print("parent p2 class m3")
class child(p1,p2):
    def m4(self):
        print("child class  m4")
obj=child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
