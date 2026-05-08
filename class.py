class Smartphone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def play_game(self):
        if self.battery >= 20:
            self.battery -= 20
            return "Playing game... 🎮"
        else:
            return "Battery too low! 🪫"

    def charge(self):
        self.battery += 10
        if self.battery > 100: self.battery = 100 # ლიმიტი 100%
        return "Charging... ⚡"

    def check_status(self):
        return f"Brand: {self.brand} | Battery: {self.battery}%"

# ტესტირება
phone = Smartphone("Honor", 87)

print(phone.play_game())     # დაიბეჭდება: Playing game...
print(phone.check_status())  # დაიბეჭდება: Brand: Honor | Battery: 67%
print(phone.charge())        # დაიბეჭდება: Charging...
print(phone.check_status())  # დაიბეჭდება: Brand: Honor | Battery: 77%

        
        
        