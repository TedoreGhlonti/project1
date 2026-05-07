import json

# ფაილის სახელი
FILE_NAME = "students.json"

# JSON-დან ჩატვირთვა
try:
    with open(FILE_NAME, "r") as f:
        students = json.load(f)

except FileNotFoundError:
    students = []


# სტუდენტის დამატება
def add_student():
    name = input("Enter name: ").strip().capitalize()
    score = int(input("Enter score: "))

    students.append({
        "name": name,
        "score": score
    })

    save_students()

    print("Student added!")


# სტუდენტების ჩვენება
def show_students():
    if len(students) == 0:
        print("No students found")
        return

    for student in students:
        print(student["name"], "-", student["score"])


# JSON-ში შენახვა
def save_students():
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)


# მთავარი მენიუ
while True:
    print("\n--- Student System ---")
    print("1. Add student")
    print("2. Show students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")