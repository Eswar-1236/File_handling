class monkey:
    def patch(self):
        print("patch() of monkey")
def monk_p(self):
    print("monk_p() from out side the class")
monkey.patch=monk_p
obj=monkey()
obj.patch()

