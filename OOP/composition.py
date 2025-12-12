#Composition :  This is when objects can contain other objects

class Engine:
    def start(self): 
        print("Engine")


#Another class Car//Car has an engine, it is not inheriting (composition)
class Car:
    def __init__(self):
        self.engine = Engine()
       
      

# #Another class that tells that car is an engine(therefore inheriting the engine)
# class car(Engine):
#     ...


##How to call the car that has engine not inheriting

car = Car()
Car.engine.start()