# # Exercise 1
# class Shape:
#     def __init__(self):
#         pass

#     def calculate_area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width


# rect = Rectangle(5, 3)
# print(rect.calculate_area())


# # Exercise 2
# class Bird:
#     def fly(self):
#         print("This Flies")


# class Mammal:
#     def run(self):
#         print ("The aniaml is running ")

# class Bat(Mammal, Bird):
#         pass



# bat1 = Bat()

# bat1.fly()
# bat1.run()


#Exercise 3
class Dog:
    def make_sound(self):
        print ("Dog is making a sound")


class Cat:
    def make_sound(self):
        print("Cat is making a sound")



class Bird:
    def make_sound(self):
        print("Bird id making a sound")
        
        
        
        
        
        
        
        
def let_them_speak(animals):
      for animal in animals:
        animal.make_sound()

animals = [Bird(),Cat(), Dog()]
let_them_speak(animals)



