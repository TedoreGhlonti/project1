import json 

DB_FILE = "students.json"

try:
    with open(DB_FILE, "r") as f:
        students = json.load(f)

except FileNotFoundError:
    students = []

def save_data():
    with open(DB_FILE, "w") as f:
        json.dump(students, f, indent=2)

while True:
    print("\n--- STUDENT SYSTEM ---")
    print("1. Show students")
    print("2. Add student")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        if len(students) == 0:
            print("No students yet.")
        else:
            for s in students:
                print(f"{s['name']} - {s['score']}")
    
    elif choice == "2":
        name = input("Enter name: ").strip().title()
        score = int(input("Enter score: "))

        students.append({
            "name": name,
            "score": score
        })

        save_data()
        print("Student added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")







