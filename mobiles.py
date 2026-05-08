import json
import os

DB_FILE = "mobiles.json"

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        mobiles = json.load(f)
else:
    mobiles = []

def save_data():
    with open(DB_FILE, "w") as f:
        json.dump(mobiles, f, indent=2)

while True:
    print("\n--- MOBILES LIST ---")
    print("1. Show phones")
    print("2. Add phones")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        if len(mobiles) == 0:
            print("No phones yet!")
        else:
            for m in mobiles:
                print(f"{m['model']} - {m['price']} - {m['year']}")
    elif choice == "2":
        model = input("Please enter model: ").strip().capitalize()
        price = int(input("Please enter price: "))
        year = int(input("Please enter year: "))

        mobiles.append({
            "model": model,
            "price": price,
            "year": year
        })

        save_data()
        print("Mobile added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


