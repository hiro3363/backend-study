products = []

def add_product():
    name = input("product: ")
    price = int(input("price: "))

    product = {
        "name": name,
        "price": price
    }
    products.append(product)

def show_products():
    for product in products:
        print(product["name"],product["price"])

def delete_product():
    name = input("delete: ")
    for product in products:
        if product["name"] == name:
            products.remove(product)
            break
while True:
    print("1. Add product")
    print("2. Show products")
    print("3. Delete product")
    print("4. Exit")

    choice = input("choice: ")

    if choice == "1":
        add_product()

    if choice == "2":
        show_products()

    if choice == "3":
        delete_product()

    if choice == "4":
        break

print("main")

