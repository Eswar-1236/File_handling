# class Account:
#     def open_account(self):
#         print("Account opend sucessfully")
#     def deposit(self):
#         print("amount deposited")
#     def with_draw(self):
#         print("amount withdraw")
#     def get_bal(self):
#         print("low bal")
# a=Account()
# a.open_account()
# a.with_draw()
# a.deposit()
# a.get_bal()


class Account:
    acc_bal=0
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount
a=Account()
a1=Account()
print(a.acc_bal)
print(a)
print(a1)
# a.deposit_amount(100)
print(a.__dict__)
print(a1.__dict__)
a.deposit_amount(100)
a1.deposit_amount(200)
print(a.__dict__)
print(a1.__dict__)


