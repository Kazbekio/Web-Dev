from models import Product, Book, Phone


def main():
    
    product = Product("Generic Product", 50, "NoBrand")
    book = Book("Atomic Habits", 20, "Penguin", "James Clear", 320)
    phone = Phone("iPhone 13", 999, "Apple", 128, 3095)

    
    products = [product, book, phone]

    
    for item in products:
        print(item.get_info())   
        print(item)              
        print("-" * 40)

    
    print(book.read())
    print(phone.call())

    
    phone.apply_discount(10)
    print("After discount:", phone.get_info())


if __name__ == "__main__":
    main()
