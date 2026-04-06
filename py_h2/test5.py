def apply_discount(price):
    new_price = price * 0.8
    return new_price

def add_tax(discounted_price):
    new_price = discounted_price * 1.18
    return new_price

def generate_receipt(final_amount):
    result = final_amount
    return f"თქვენი გადასახდელია: {final_amount:.2f} ლარი. გმადლობთ!"

user = int(input("Please enter price: "))
final_price = apply_discount(user)
result2 = add_tax(final_price)
result3 = generate_receipt(result2)

print(result3)








  