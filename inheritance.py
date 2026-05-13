class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

class Lightcars(Car):

    def cars_info(self):

        return f"Car: {self.brand}, Year: {self.year}, Color: {self.color}"
    
class Trucks(Car):

    def cars_info(self):

        return f"Truck: {self.brand}, Year: {self.year}, Color: {self.color}"
    
car1 = Lightcars("Mercedes", 2022, "black")
car2 = Lightcars("BMW", 2025, "red")
truck1 = Trucks("Scania", 2023, "orange")
truck2 = Trucks("DAF", 2024, "white")

car_list = [car1, car2, truck1, truck2]

print("--- CAR LIST ---")
print("-" * 20)

for c in car_list:
    print(c.cars_info())

print("-" * 20)

        



        
        