from abc import *
class test(ABC):
    @abstractmethod
    def cal_tax(self):
        pass
b=test()
print(id(b))