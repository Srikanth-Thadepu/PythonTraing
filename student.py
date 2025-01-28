class School:
    def __init__(self):
        self.name="Srikanth"
        self.id="7"
    def display_school(self):
        print(f"The Name and ID of the student are: {self.name} {self.id}")

class College(School):
    def __init__(self):
        super().__init__()
        self.branch="ECE"
        self.grade=8

class PG(College):
    def __init__(self):
        super().__init__()
        self.specialization="communication"

student=PG()
student.display_school()
print(student.branch)
print(student.grade)