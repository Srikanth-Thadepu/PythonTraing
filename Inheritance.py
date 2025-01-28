class Parent:
    def __init__(self):
        self.bignose="7cm"
    
    def display_parent(self):
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        
    def display_child(self):
        print("This is the child class")

child=Child()
child.display_parent()
child.display_child()
print(child.bignose)