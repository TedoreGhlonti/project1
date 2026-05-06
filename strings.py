students = []

def add_student(name, score):
    students.append({"name": name, "score": score})


def show_students():
    for student in students:
        print(student["name"], "-", student["score"])

def find_student(name):
    for student in students:
        if student["name"] == name:
            print("Found:", student)
            return
    print("Student not found")

def remove_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Removed:", name)
            return
    print("Student not found")  

while True:
    print("\n1. Add student")
    print("2. Show students")
    print("3. Find student")
    print("4. Remove student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(name, score)

    elif choice == "2":
        show_students()

    elif choice == "3":
        name = input("Enter name: ")
        find_student(name)

    elif choice == "4":
        name = input("Enter name: ")
        remove_student(name)

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice")  


    
    
    










