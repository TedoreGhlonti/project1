# 1. გვაქვს ლექსიკონი
accounts = {"Gogi": 100, "Ani": 50}

# 2. ვწერთ ფუნქციას
def bank_system(database, user, amount):
    if user in database:
        database[user] += amount
        
    else:
        database[user] = amount

    return database

print(bank_system(accounts, "Lasha", 30))
  
    










