class InsufficiantException(Exception):
    def __init__(self,msg)-> None:
        self.msg=msg
def withdraw():
    try:
        amount=int(input("enter your amount for withdrawl"))
        bal=500
        if bal>amount:
            print("sufficiant amount withdrawl and fundago enjoy")
        else:
            raise InsufficiantException("low fund balence")
        
    except InsufficiantException as err:
        print(err.msg)
withdraw()
print("good morning")
    