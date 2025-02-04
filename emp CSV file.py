import csv

class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "Employee ID": self.id,
            "Name": self.name,
            "Department": self.department,
            "Salary": self.salary
        }

employees = [
    Employee("1", "Srikanth", "Developer", "50000"),
    Employee("2", "Shashwath", "Finance", "50000"),
    Employee("3", "JP", "R&D", "50000")
]

csv_file = "employees.csv"

with open(csv_file, mode='a', newline='') as file:
    fieldnames = ["Employee ID", "Name", "Department", "Salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for emp in employees:
        writer.writerow(emp.to_dict())

print(f"New employees have been appended to the CSV file '{csv_file}' successfully!")