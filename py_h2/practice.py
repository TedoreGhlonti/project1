people = [
    {"name": "Alice", "age": 25, "salary": 3000},
    {"name": "Bob", "age": 17, "salary": 1500},
    {"name": "Mike", "age": 19, "salary": 1800},
    {"name": "Anna", "age": 15, "salary": 1000},
    {"name": "Tedore", "age": 44, "salary": 2500}
]

# 1️⃣ საშუალო ასაკი
total_age = 0
for user in people:
    total_age += user["age"]
average_age = total_age / len(people)
print(f"Average age: {average_age:.2f}")

# 2️⃣ ყველაზე მაღალი salary
max_salary = 0
max_salary_user = ""
for user in people:
    if user["salary"] > max_salary:
        max_salary = user["salary"]
        max_salary_user = user["name"]
print(f"Highest salary: {max_salary_user} ({max_salary})")

# 3️⃣ senior_high_income
senior_high_income = []
for user in people:
    if user["age"] >= 18 and user["salary"] > 2000:
        senior_high_income.append(user)
print("Senior high income:", senior_high_income)



        









    

