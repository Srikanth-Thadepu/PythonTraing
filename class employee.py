class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary
    
    def allowance(self,allowance):
        self._salary+=allowance
        return allowance
    
    def deduction(self,deduction):
        self._salary-=deduction
        return deduction

emp = Employee("Alice", 50000)
print("Salary before update: ", emp.get_salary())
emp.set_salary(60000)
print("Salary after update: ", emp.get_salary())
emp.allowance(5000)
print("Salary after Allowance: ",emp.get_salary())
emp.deduction(1000)
print("Salary after deduction: ",emp.get_salary())