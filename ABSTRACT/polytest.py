from polymorphism import*
def exec(obj):
    obj.cal_tax()
#collect(10)#'int' object has no attribute 'cal_tax'
exec(Employe())
exec(Account())
exec(user())