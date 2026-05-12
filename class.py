class Smartphone():
    def __init__(self, model):
        self.model = model
        self.battery = 100

    def use_app(self, cost):
        self.battery -= cost
        
        # თუ ბატარეა 0-ს ჩამოსცდა
        if self.battery <= 0:
            self.battery = 0
            print("Phone is dead")

    def charge(self, amount):
        self.battery += amount
        
        # თუ ბატარეა 100-ს გადასცდა
        if self.battery > 100:
            self.battery = 100

my_phone = Smartphone("Samsung")
my_phone.use_app(120) # ვაკლებთ იმაზე მეტს, რაც გვაქვს
print(f"Battery: {my_phone.battery}%") # დაბეჭდავს 0-ს და არა -20-ს


        
        
        
        
        
        

        
        
        
        
        
    
        


        
        
        
        
        

        


        
        

        

        
        
        