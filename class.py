class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):

        return f"Brand: {self.brand} | Year: {self.year}"
    
result = Car("BMW", 2022)
print(result.show_info())