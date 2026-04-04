correct_pin = 211  
attempts = 0       

while attempts < 3:
    try:
        user_pin = int(input("Enter PIN: "))

        if user_pin == correct_pin:
            print("Access Granted! 💰")
            break
        else:
            attempts += 1
            remaining = 3 - attempts
            print(f"Wrong PIN! You have {remaining} attempts left.")

    except ValueError:
        attempts += 1
        remaining = 3 - attempts
        print(f"Invalid input! Use numbers only. {remaining} attempts left.")
if attempts == 3:
    print("Card Blocked! ❌ Please contact your bank.")
