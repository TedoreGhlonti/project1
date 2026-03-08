students = [
    {"name": "Anano", "age": 22, "subject": "PHP"},
    {"name": "Luka", "age": 20, "subject": "Data Science"},
    {"name": "Mari", "age": 21, "subject": "Web Design"},
    {"name": "Tedore", "age": 43, "subject": "Python"}
]

for student in students:
    if student["age"] > 30:
        print(f"Name: {student['name']}, Age: {student['age']}")