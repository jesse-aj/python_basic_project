class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_student_info(self):
        student_info = f"{self.name} is a student of Aggrey and he is {self.age} years old!"
        return student_info


first_student = Student("Jesse", "18")
print(first_student.view_student_info())
