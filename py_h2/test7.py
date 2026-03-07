cars = [
    {"brand": "BMW", "model": "M5", "price": 35000},
    {"brand": "Mercedes", "model": "G63", "price": 45000},
    {"brand": "Audi", "model": "Q7", "price": 55000}
]

# 1. ძებნის ფუნქცია
def search_car(cars_list, brand_name):
    for car in cars_list:
        if car["brand"].lower() == brand_name.lower():
            return f"{car['brand']} {car['model']} price is: {car['price']}$"
    return "Brand not found!"

# 2. დამატების ფუნქცია
def add_new_car(cars_list):
    brand = input("enter brend: ")
    model = input("enter model: ")
    price = int(input("enter price: "))
    
    new_car = {"brand": brand, "model": model, "price": price}
    cars_list.append(new_car)
    print("car added sucessfully!")
action = input("Choose option (search/add/exit): ").lower().strip()

if action == "search":
    user_query = input("Which brand do you search?: ")
    print(search_car(cars, user_query)) 
elif action == "add":
    add_new_car(cars) 
    print("Updated list:", cars)
elif action == "exit":
    print("Bye!")
else:
    print("Wrong command!")





            
            
