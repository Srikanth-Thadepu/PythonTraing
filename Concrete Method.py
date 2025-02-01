from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete Method")

class Son(Father):
    def disp(self):
        print("Son is implementing the abstract method")

class Daughter(Father):
    def disp(self):
        print("Daughter is implementing the abstract method")

son=Son()
daughter=Daughter()
son.disp()
daughter.disp()