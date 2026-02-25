passengers = [
    {"name": "Lasha", "items": ["phone", "laptop", "water"]},
    {"name": "Unknown", "items": ["gun", "map"]},
    {"name": "Mari", "items": ["book", "knife", "candy"]},
    {"name": "Terminator", "items": ["sunglasses", "mission_file"]}
]

for person in passengers:
    if person["name"] == "Terminator":
        print("SYSTEM FAILURE - TARGET IDENTIFIED!")
        break
    elif "gun" in person["items"] or "knife" in person["items"]:
        print(f"Alert! {person['name']} is carrying dangerous items!")
        continue
    else:
        print(f"Welcome, {person["name"]}! Have a nice flight!")

            
            



