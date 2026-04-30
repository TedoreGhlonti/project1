import json
import os

DB_FILE = "my_car.json"

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("--- მონაცემები წარმატებით შეინახა ---")

def load_data():
    if not os.path.exists(DB_FILE):
        return {} 
    
    with open(DB_FILE, "r") as file:
        return json.load(file)

initial_car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "owners": ["Tedore"]
}

save_data(initial_car)

my_car = load_data()

my_car["owners"].append("Giorgi")
my_car["year"] = 2024

save_data(my_car)

final_data = load_data()
print(f"Owners: {final_data['owners']}")
print(f"Year: {final_data['year']}")