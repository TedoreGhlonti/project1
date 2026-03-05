inventory = [
    {"product": "iPhone", "price": 1200},
    {"product": "Samsung", "price": 900},
    {"product": "MacBook", "price": 2500},
    {"product": "Xiaomi", "price": 400}
]

max_price = 0
expensive_product = ""
for item in inventory:
    if item["price"] > max_price:
        max_price = item["price"]
        expensive_product = item["product"]

print(f"Most expencive is {expensive_product} price: {max_price}")



         
        
