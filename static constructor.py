class Student:
    student_count = 0

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        Student.student_count += 1

student1 = Student("Alice", 1)
student2 = Student("Bob", 2)

print(f"Total students: {Student.student_count}")