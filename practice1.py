basket = [
    {"item": "Nike Air Max", "total_paid": 450, "quantity": 3},
    {"item": "Adidas Socks", "total_paid": 60, "quantity": 0},  # აქ შეცდომაა (0)
    {"item": "Puma Tee", "total_paid": 100, "quantity": "ორი"}, # აქაც შეცდომაა (ტექსტი)
    {"item": "Reebok Cap", "total_paid": 80, "quantity": 2}
]

def calculate_unit_price(total_amount, quantity):
    try:
        return total_amount / quantity
    except ZeroDivisionError:
        return "Error: quantity could not be zero!"
    except TypeError:
        return "info must be in numbers!"
    except KeyError as e:
        return "There is no key"
for product in basket:
    try:
     name = product["item"]
     total = product["total_paid"]
     qty = product["quantity"]
    except KeyError as e:
        print("There is no key")
    result = calculate_unit_price(total, qty)
    print(f"{name} - Unit Price: {result}")

    





