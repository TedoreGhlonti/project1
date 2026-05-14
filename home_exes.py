class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_level = 100

    def describe_phone(self):
        return f"{self.brand} {self.model} | Price: ${self.price} | Battery: {self.battery_level}%"
    
    def reduce_battery(self, amount):
        self.battery_level -= amount
        if self.battery_level < 0:
            self.battery_level = 0
        return f"Battery decreased to {self.battery_level}%"

class Samsung(Smartphone):
    def power_share(self):
        return "Wireless power sharing is now active..."

class Apple(Smartphone):
    def face_id_unlock(self):
        return "Scanning face... Identity confirmed. Unlocked!"

class MobileShop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.inventory = []

    def add_phone(self, phone):
        self.inventory.append(phone)
        return f"SUCCESS: {phone.brand} {phone.model} added to inventory."

    def sell_phone(self, model_name):
        """Removes a phone from inventory if found by model name"""
        for phone in self.inventory:
            if phone.model == model_name:
                self.inventory.remove(phone)
                return f"SALE: {phone.brand} {phone.model} has been sold!"
        return f"ERROR: Model '{model_name}' not found in stock."

    def show_inventory(self):
        print(f"\n--- Welcome to {self.shop_name} ---")
        if not self.inventory:
            print("Status: Out of stock.")
        else:
            for phone in self.inventory:
                print(f"-> {phone.describe_phone()}")

p1 = Samsung("Samsung", "S23 Ultra", 1200)
p2 = Apple("Apple", "iPhone 15 Pro", 1400)

my_shop = MobileShop("TechZone")
print(my_shop.add_phone(p1))
print(my_shop.add_phone(p2))

my_shop.show_inventory()

print(my_shop.sell_phone("S23 Ultra"))

my_shop.show_inventory()