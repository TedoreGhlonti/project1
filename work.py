class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

class Mycar(Car):

    def drive(self):

        return f"You are driving {self.year} {self.color} {self.brand}"
    
class ElectricCar(Car):

    def drive(self):

        return f"You are driving {self.year} {self.color} {self.brand} silently... ⚡"
    
    def charge(self):
        return "Charging the battery..."
    
class Truck(Car):

    def drive(self):

        return f"You are driving {self.year} {self.color} a heavy {self.brand}"
    
    def load_cargo(self):

        return f"Cargo is loaded!"
    
my_car = Mycar("Hyundai", 2013, "brown")
my_car1 = Mycar("Mustang", 2020, "red")
my_car2 = Mycar("Mercedes", 2025, "black")
tesla = ElectricCar("Tesla", 2023, "white")
truck = Truck("Scania", 2022, "yellow")
print(my_car.drive())
print(my_car1.drive())
print(my_car2.drive())
print(tesla.drive())
print(tesla.charge())
print(truck.drive())
print(truck.load_cargo())

        

