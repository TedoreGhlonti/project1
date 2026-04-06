
my_cart = []

while True:
    user = input("Product name (or 'done'): ")

    if user == "done":
        break

    price = float(input("Price: "))

    product_entry = {"item": user, "price": price}


    my_cart.append(product_entry)

    print(product_entry)

       



