people = [
    {"name": "Alice", "age": 25, "salary": 3000},
    {"name": "Bob", "age": 17, "salary": 1500},
    {"name": "Mike", "age": 19, "salary": 1800},
    {"name": "Anna", "age": 15, "salary": 1000},
    {"name": "Tedore", "age": 44, "salary": 2500}
]

numbers = [4, -3, 0, 7, -10, 15, 2, -1, 2, 2]

# ცვლადები
sum_age = 0
max_salary = people[0]["salary"]
max_salary_user = people[0]["name"]
senior_high_income = []

positive_count = 0
positive_min = None
negative_count = 0
negative_max = None
two_count = 0
numbers_without_two = []

# loop people
for user in people:
    # საშუალო ასაკი
    sum_age += user["age"]
    
    # max salary
    if user["salary"] > max_salary:
        max_salary = user["salary"]
        max_salary_user = user["name"]
    
    # senior high income
    if user["age"] >= 18 and user["salary"] > 2000:
        senior_high_income.append(user)

# loop numbers
for n in numbers:
    if n > 0:
        positive_count += 1
        if positive_min is None or n < positive_min:
            positive_min = n
    elif n < 0:
        negative_count += 1
        if negative_max is None or n > negative_max:
            negative_max = n
    if n == 2:
        two_count += 1
    else:
        numbers_without_two.append(n)

# საბოლოო output
average_age = sum_age / len(people)
print(f"Average age: {average_age:.2f}")
print(f"Highest salary: {max_salary_user} ({max_salary})")
print("Senior high income:", senior_high_income)
print(f"Positive count: {positive_count}, Positive min: {positive_min}")
print(f"Negative count: {negative_count}, Negative max: {negative_max}")
print(f"Number of 2's: {two_count}, Numbers without 2: {numbers_without_two}")





