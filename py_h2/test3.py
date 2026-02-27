employees = [
    {"name": "ნიკა", "role": "Developer", "salary": 2000},
    {"name": "ანა", "role": "Manager", "salary": 3000},
    {"name": "გიორგი", "role": "Developer", "salary": 2500}
]

for employee in employees:
    if employee["role"] == "Developer":
        employee["salary"] += 500
    elif employee["role"] == "Manager":
        employee["bonus"] = [100, 200]
        employee["bonus"].append(500)

print(employees)
   







            
            



