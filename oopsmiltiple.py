class parent1:
    def m1(self):
        print("parent 1 class of m1")
    def m2(self):
        print("paren1 class of m2")
class parent2:
    def m3(self):
        print("parent2 class of m3")
    def m4(self):
        print("paren2 class of m4")
class child(parent1,parent2):
    def m5(self):
        print("child class of m5 method")
obj=child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
obj.m5()

