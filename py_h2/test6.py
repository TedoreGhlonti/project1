inventory = [
    {"product": "iPhone", "price": 1200},
    {"product": "Samsung", "price": 900},
    {"product": "MacBook", "price": 2500},
    {"product": "Xiaomi", "price": 400}
]

max_price = 0

for item in inventory:
    if item["price"] > max_price:
        max_price = item["price"]


print(max_price)



         
        
