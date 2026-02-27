cities = [
    {"name": "Tbilisi", "population": 1100000},
    {"name": "Batumi", "population": 170000},
    {"name": "Kutaisi", "population": 140000}
]
big_cities = []
for city in cities:
    if city["population"] > 500000:
        city["is_big"] = "yes"
        big_cities.append(city)
    else:
        city["is_big"] = "no"

    
print(cities)
print(big_cities)
   
   







            
            



