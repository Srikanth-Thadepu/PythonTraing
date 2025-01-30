class Employee:
    def __init__(self,name,designition,salary):
        self.name=name
        self.designition=designition
        self.salary=salary
    
    def display(self):
        print(f"The Employee's datails are, Name: {self.name}, Designition: {self.designition}, Salary: {self.salary}")

emp=[]

emp.append(Employee("Srikanth",'Developer',"400000"))
emp.append(Employee("Shashwath","Data Analyst",'400000'))
emp.append(Employee("Jaya Prakash","Senior Developer","500000"))

for i in emp:
    i.display()