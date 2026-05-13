class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

class Lightcar(Car):

    def action(self, speed):
     message = f"You are driving {self.year} {self.brand} at {speed} km/h."
     if speed > 120:
        return message + " WARNING: Slow down!"
    
    
     return message + " Normal speed!"
        
    def car_age(self):
     current_year = 2026
     age = current_year - self.year
     return f"This {self.brand} is {age} years old."

car1 = Lightcar("Mercedes", 2025, "black")
car2 = Lightcar("Audi", 2024, "red")
car3 = Lightcar("Mustang", 2023, "red")
print(car1.action(90))
print(car1.car_age())
print(car2.action(140))
print(car2.car_age()) 
print(car3.action(150))
print(car3.car_age())       
        
        
        
        


        
        
        



        
        