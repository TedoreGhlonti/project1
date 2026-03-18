products = {"iphone": 1000, "macbook": 2000, "ipad": 500}

def get_price(name):
    if name in products:
        return products[name]
    else:
        return "Product not found"


user = input("Enter name: ").lower()    
result = get_price(user)
print(result)
    

