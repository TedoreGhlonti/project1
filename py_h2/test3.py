inventory = {
    "Apple": 10,
    "Banana": 0,
    "Orange": 5,
    "Milk": 0
}

for key, value in inventory.items():
    if value == 0:
        print(f'{key} is out of stock!')
    else:
        print(f'{key}: {value}')

inventory["Milk"] = 12
inventory["Orange"] -= 2
print(inventory)   
            
            



