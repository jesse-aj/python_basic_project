import csv


class Product:
    # class level attrubute
    pay_rate = 0.8  # Pay after discount
    all = []




    # instance attribute
    def __init__(self, name: str, price: float, quantity=0):
        # Run  validation to the recieved arguments

        assert price >= 0, F"Price {price} is not greater or equal to zero"
        assert quantity >= 0, F"Price {quantity} is not greater or equals than zero"

        # Assign each to self object
        self.name = name
        self.price = price
        self.quantity = quantity





        # Actions to execute
        Product.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate







    @classmethod
    # this cannot take self because it will be too much confusing cause it is a class method  so it takes cls as the parameter which is refrence for class
    def instantiate_from_csv(cls):
        with open('oop.csv', 'r') as f:  # context manager that read the csv file
            reader = csv.DictReader(f)  # it transfers it too, to dictionary
            list_Products = list(reader)  # This makes it a list
        for products in list_Products:
            Product(
                name=products.get("name"),
                price=float(products.get("price")),
                quantity=float(products.get("quantity"))
            )






    @staticmethod
    def is_integer(num):  #The static method does not recieve class as the parameter as class method do
         ##We will count out the floats that are points zero 
         if isinstance(num, float):
             #count out the float that are points zero
             return num.is_integer()
         elif isinstance(num, int):
             return True
         else:
             False
             




# Magic methods __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}'. {self.price}, {self.quantity})"


##Actions
# print(Product.is_integer(556))
# Product.instantiate_from_csv()
# print(Product.all)  # Will print all instances


# To print all name of intance using for loops
# for instance in Product.all:
#      print(instance.name)

class Phone(Product):
 
     def __init__(self, name: str, price: float, quantity=0, broken_phones=0 ):

        #call to super function to have access to all/ atrributes / methods
        super().__init__(name , 
                          price , quantity)
        # Run  validation to the recieved arguments
        assert broken_phones >=0, f"Broken phones{broken_phones} is not greater or equal to zero"

        # Assign each to self object
        self.broken_phones = broken_phones

