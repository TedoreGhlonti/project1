import json
import os

DB_FILE = "fr.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"fruits": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)
    
def save_db(fr):
    with open(DB_FILE, "w") as f:
        json.dump(fr, f, indent=2)

def register():
    fruit = input("Choose a fruit: ").strip()
    if not fruit:
        print("Fruit can not be empty!")
        return
    fr = load_db()
    if fruit in fr['fruits']:
        print("That username already exists.")
        return
    fr["fruits"][fruit] = {
        "fruit": fruit,
        "quantity": 0.0
    }

    save_db(fr)
    print(f"Item added!")

while True:
    print("\n --- fruits list ---")
    print("1. Add fruit")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choise")