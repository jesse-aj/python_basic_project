## Having attributes and methods being inherited from another class


##Parent class (SuperClass)
class Mamal:
    num_of_mamals = 0

    def __init__(self):
        Mamal.num_of_mamals += 1

    def speak(self):
        raise NotImplementedError("Subclasses must implement this")
    


##Child or inherited class (Sub class)
class snake(Mamal):
    def speak (self):
        return "sssssss"

class human(Mamal):
    def speak(self):
        return "here here come here"



animals = [human(), snake()]


for animal in animals:
    print(animal.speak())




####POLY MORPHISM #####   Using it for different form( Simmillar as looping through to perform an action on all mamals)

def make_it_speak(Mamal):
    print(Mamal.speak(), Mamal.num_of_mamals)



make_it_speak(human())
make_it_speak(snake())