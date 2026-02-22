students = ["Anna", "Giorgi", "Lasha", "Tedore", "Mariami"]
grades =   [57, 68, 82, 88, 95]

# students[0] = grades[0]  <-- ეს ხაზი ამოვშალეთ

def add_student(name, point):
    if name != "" and 0 <= point <= 100:
        students.append(name)
        grades.append(point)
        print(f'{name} added successfully!')
    else:
        print('Wrong! Name is empty or point is incorrect!')

def remove_student(name):
    if name in students:
        i = students.index(name)
        students.pop(i)
        grades.pop(i)
        print(f'{name} removed successfully!')
    else:
        print(f'Error: Student {name} not found!')

def display_all():
    for i in range(len(students)):
        # აი აქ გასწორდა grades[i]
        print(f'{students[i]} - {grades[i]}')

def calculate_average():
    if len(grades) == 0:
        print("The list is empty, cannot calculate average.")
    else:
        total_sum = sum(grades)
        count = len(grades)
        average = total_sum / count
        print(f"The average grade of the class is: {average}")

# ახლა შეგიძლია გამოიძახო ნებისმიერი მათგანი:
display_all()
calculate_average()