class Accaunt():

    def __init__(self, balance):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
    
    def withdraw(self, amount):

        self.balance -= amount
    
    def display(self):

        return f"Current balance: {self.balance}"
    
result = Accaunt(500)
result.deposit(200)
result.withdraw(100)
print(result.display())

        
        
        
        
        
    
        


        
        
        
        
        

        


        
        

        

        
        
        