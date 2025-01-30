class Employee:
    def __init__(self, *emp_details):
        if len(emp_details) == 1:
            print(f"Hello {emp_details[0]}")
        elif len(emp_details) == 2:
            print(f"Hello {emp_details[0]}, your ID is {emp_details[1]}")

emp1 = Employee("Sk", '7')
emp2 = Employee("xyz", 101)

class Employee:
    def __init__(self, **details):
        if "name" in details and "id" in details:
            print(f"Hello {details['name']}, your ID is {details['id']}")

emp3 = Employee(name="Srikanth", id=102)

class Deconstructor:
    def __init__(self, name):
        self.name = name  
        print(f"Employee {self.name} has joined")

    def __del__(self):
        print(f"Employee {self.name} has resigned")

emp4 = Deconstructor("xyz")
del emp4