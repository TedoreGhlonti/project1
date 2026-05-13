class Fruit:
    fruits_list = []

    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        
        Fruit.fruits_list.append(self)

class List(Fruit):
    def info(self):
        total = self.price * self.quantity
        return f"Item: {self.item:<7} | Total Value: {total:>6} GEL"


fr1 = List("Apple", 2.5, 30)
fr2 = List("Banana", 3.5, 35)
fr3 = List("Kiwi", 2.8, 45)

print("--- Fruits Detailed List ---")
for f in Fruit.fruits_list:
    print(f.info())
        
        


        
        
        



        
        