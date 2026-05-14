class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restourant(self):

        return f"Welcome to {self.restaurant_name}, We serve delicious {self.cuisine_type} cuisine.!"
        
        
    
    def open_restaurant(self):
        return f"The restaurant {self.restaurant_name} is now OPEN!"
    
    def set_number_served(self, number):
        self.number_served = number
        return f"Number of served customers set to {self.number_served}."

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers
        return f"Served {additional_customers} more customers. Total now: {self.number_served}."



    
res1 = Restaurant("Pasanauri", "Georgian")
print(res1.describe_restourant())
print(res1.open_restaurant())
print(res1.set_number_served(10))
print(res1.increment_number_served(5))
res2 = Restaurant("Pomodissimo", "Italian")
print(res2.describe_restourant())
print(res2.open_restaurant())
print(res2.set_number_served(15))
print(res2.increment_number_served(15))
res3 = Restaurant("Tokyo House", "Asian")
print(res3.describe_restourant())
print(res3.open_restaurant())
print(res3.set_number_served(7))
print(res3.increment_number_served(12))

      
    

        