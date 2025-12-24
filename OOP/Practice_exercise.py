
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} and will be a billionaire"

#     def __del__(self):
#         return "Goodbyeeee"


# Person1 = Person("Jesse", 18)
# print(Person1)

# # Exercise 2


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"{self.title} was written by {self.author} and it has {self.pages} pages"


# book1 = Book("Laws of power", "Jesse Appiah", 200)
# print(book1)


# Exercise 3
class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def is_wild(self):
        wild = f"{self.name} is a wild dog"
        return wild

    def __repr__(self):
        return f"Does this {self.name} eat? {self.eat} " f"\nDoes this {self.name} sleep? {self.sleep}"




class Dog():
    def __init__(self, animal, bark):
        self.animal = animal   #composition
        self.bark = bark


    def can_bark_loud(self):
        loud_bark = f"{self.animal.name} can bark louddddd, very loudddd"
        return loud_bark
    
animal1 = Animal("Scooby", True, False)
doggo = Dog(animal1, True)

print(doggo.can_bark_loud())
print(doggo.animal.is_wild())
print(doggo.animal.name)
print(doggo.animal)