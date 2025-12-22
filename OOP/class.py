class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

    def view_student_info(self):
            self.name = input("Please Enter your name: ")
            self.age = int(input("Enter your age: "))
            student_info = f"{self.name} was a student of Aggrey and he is {self.age} years old!"
            print(student_info)
            return student_info

    def check_age(self):
        student_age = self.age
        if student_age < 50:
            print("Welcome")
        else:
            print("You are old to be admitted by as student buh anything buh anything is posible")
            




##This is the objects

first_student = Student()
second_student = Student()
third_student = Student()

## This performs actions to the objects
print("\n--First Student Querry----")
first_student.view_student_info()
first_student.check_age()

print("\n--Second Student Querry----")
second_student.view_student_info()
first_student.check_age()

print("\n--Third Student Querry----")
third_student.view_student_info()
third_student.check_age()



