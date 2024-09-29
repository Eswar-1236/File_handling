class Grand_p:
    def m(self):
        print("grand parent class m")
    def m1(self):
        print("grand parent class m1")
class parent(Grand_p):
    def m2(self):
        print(" parent class m2")
class child(parent):
    def m3(self):
        print("child class m3")
obj=child()
obj.m()
obj.m1()
obj.m2()
obj.m3()
