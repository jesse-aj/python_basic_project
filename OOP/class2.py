class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_value(self):
        Total_product_value = self.price * self.quantity
        return f"The total value of {self.name} is {Total_product_value}"


prod1 = Product("Rice", 20, 6)
print(prod1.calculate_value())
