import json

person = {
    "name": "Ana",
    "age": 22
}

with open("person.json", "w") as f:
    data = json.dump(person, f, indent=2)

with open("person.json", "r") as f:
    data1 = json.load(f)

print(data1["name"])