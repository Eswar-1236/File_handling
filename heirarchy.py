class p1:
    def m1(self):
        print("p1 class method m1")
class ch1(p1):
    def m2(self):
        print("ch1 clas method m2")
class ch2(p1):
    def m3(self):
        print("ch2 calss m3")
obj=ch1()
obj.m1()
obj.m2()
ob=ch2()
ob.m1()
ob.m3()
