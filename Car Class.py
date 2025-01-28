class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"The car is a {self.brand} {self.model}")

car1=Car("Toyota","Corolla")
car2=Car("Suzuki","Swift")
car1.display()
car2.display()