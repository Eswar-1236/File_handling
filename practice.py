class Accont:
    bank_name="STATE BANK OF INDIA"
    min_balnece=2000
    def __init__(self,name,acc_no,address,phno) -> None:
         self.name=name
         self.acc_no=acc_no
         self.address=address
         self.phno=phno

a=Accont("ESWAR NAIK",12343222,"ANANTAPUR",9381432701)
# a.m1
print(a.__dict__)
