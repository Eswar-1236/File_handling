from abc import *
class test:
    @abstractmethod
    def cal_tax(self):
        pass
b=test()
print(b)
print(id(b))
