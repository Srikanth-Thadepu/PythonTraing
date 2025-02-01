from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

class Child(Father):
    def disp(self):
        print("This is Child Class")
        print("Printing Abstract Method")

class Other_Child(Father):
    def disp(self):
        print("This is another Child Class")
        print("Printing Abstract Method")

a=Child()
b=Other_Child()
a.disp()
b.disp()