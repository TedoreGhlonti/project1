import time
import random
from plyer import notification

# 1. Configuration
config = {
    "interval": 60 * 60,  # 20 minutes (Real mode)
    "app_name": "Eye Care Assistant",
    "notification_title": "Time to Break! 👀"
}

# 2. Health Tips List
advices = [
    "Drink a glass of water! 💧",
    "Stretch your body and sit up straight! 🧘‍♂️",
    "Blink your eyes rapidly 10 times! ✨",
    "Look at an object far away for 20 seconds! 🔭",
    "Stand up and walk around for a minute! 🚶‍♂️",
    "Take a deep breath and relax your shoulders! 🌬️"
]

print("Your Eye Care Assistant is now active! Stay healthy. 🔥")

while True:
    time.sleep(config["interval"])
    
    # Pick a random tip
    current_advice = random.choice(advices)
    
    # Send notification
    notification.notify(
        title=config["notification_title"],
        message=current_advice,
        app_name=config["app_name"],
        timeout=15
    )