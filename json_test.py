import json

me = {
    "name": "Tedore",
    "age": 25,
    "city": "Ozurgeti",
    "skills": ["Python", "Farming", "Logic"]
}

db_file = "me.json"

with open(db_file, "w") as f:
    json.dump(me, f, indent=2)

print(f"File {db_file} created!")

with open(db_file, "r") as f:
    data = json.load(f)

print(data)

