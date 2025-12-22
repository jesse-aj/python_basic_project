class Dog:
   
   ##A method is a function in a class(Below is a method of the class dog)

   #Attributes using functions(method)
   #__init__ is the constructor for creating attributes and self is used to create an instance
   def __init__(self, name, age):
      self.name = name
      self.age = age

      

    #Actions using functions(method)
   def bark(self):
      print(f"{self.name} is making barking")


##The objects itself 

scooby = Dog("scobby", 50)
humble = Dog("humble", 30)


scooby.bark()
humble.bark()



























