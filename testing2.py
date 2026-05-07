import json

students = [
    {"name": "Gio", "score": 90},
    {"name": "Nika", "score": 80}
]

with open("students.json", "w") as f:
    data = json.dump(students, f, indent=2)

with open("students.json", "r") as f:
    data1 = json.load(f)

print(data1[1]["score"])