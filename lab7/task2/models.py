class Product:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def get_info(self):
        return f"{self.name} by {self.brand}, price: {self.price}$"

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, brand={self.brand})"


#childclass1
class Book(Product):
    def __init__(self, name, price, brand, author, pages):
        super().__init__(name, price, brand)
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"Book: {self.name} by {self.author}, {self.pages} pages, price: {self.price}$"

    def read(self):
        return f"You are reading '{self.name}' by {self.author}"

    def __str__(self):
        return f"Book(name={self.name}, author={self.author}, price={self.price})"


# 2
class Phone(Product):
    def __init__(self, name, price, brand, storage, battery):
        super().__init__(name, price, brand)
        self.storage = storage
        self.battery = battery

    def get_info(self):
        return f"Phone: {self.name}, {self.storage}GB, battery: {self.battery}mAh, price: {self.price}$"

    def call(self):
        return f"Calling from {self.name}..."

    def __str__(self):
        return f"Phone(name={self.name}, storage={self.storage}GB, price={self.price})"