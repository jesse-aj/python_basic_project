from Product_class import Product

class Phone(Product):
 
     def __init__(self, name: str, price: float, quantity=0, broken_phones=0 ):

        #call to super function to have access to all/ atrributes / methods
        super().__init__(name , 
                          price , quantity)
        # Run  validation to the recieved arguments
        assert broken_phones >=0, f"Broken phones{broken_phones} is not greater or equal to zero"

        # Assign each to self object
        self.broken_phones = broken_phones
