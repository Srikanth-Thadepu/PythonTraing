from abc import ABC, abstractmethod
from typing import List

class Employees(ABC):

    @abstractmethod

    def work(self):
        pass

    @abstractmethod

    def get_salary(self):
        pass

class Manager(Employees):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    
    def work(self) -> str:
        return f"{self.name} is managing the team."
    
    def get_salary(self) -> float:
        return self.salary

class Developer(Employees):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    
    def work(self) -> str:
        return f"{self.name} is writing a code"
    
    def get_salary(self) -> float:
        return self.salary

class Intern(Employees):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary

    def work(self) -> str:
        return f"{self.name} is learning and assisting"
    
    def get_salary(self)->float:
        return self.salary

class Security(Employees):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    
    def work(self) -> str:
        return f"{self.name} is guarding"
    
    def get_salary(self)->float:
        return self.salary
    
class Department:
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
        self.employees:List[Employees]=[]
    
    def hire(self,employee:Employees)->None:
        self.employees.append(employee)
        print(f"{employee.name} is hired")

    def fire(self,employee:Employees)->None:
        self.employees.remove(employee)
        print(f"{employee.name} is fired")
    
    def promote(self,employee:Employees)->None:
        employee.salary+=2000
        print(f"{employee.name} is promoted and salary is incremented to {employee.salary}")
    
    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)
    
    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
securitystaff=Security("Ram",5000)

it_department = Department("IT",50000)

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)
it_department.promote(developer)
it_department.fire(intern)
it_department.show_employee_details()

total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")