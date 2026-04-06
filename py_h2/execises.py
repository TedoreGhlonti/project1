user_name = input("Please enter your name: ").strip().capitalize()
balance = 500
user_id1 = "0211"
total_try = 3

while True:
    print("\n" + "="*20)
    print("      ATM MENU")
    print("="*20)
    print("1. Enter PIN")
    print("2. Check Balance")
    print("3. Withdraw Cash")
    print("4. Exit")
    
    choice = input("\nPlease choose an option (1-4): ")

    if choice == "1":  
        user_id = input("Please enter PIN: ")
        hidden_version = "*" * len(user_id)
        
        if user_id == user_id1:
            print(hidden_version)
            print("Access Granted!")
        else:
            total_try -= 1
            print(f"Wrong PIN! You have {total_try} attempts left.")
            if total_try == 0:
                print("Your card is blocked! System shutting down.")
                break 

    elif choice == "2": 
        print(f"\nAccount Holder: {user_name}")
        print(f"Current Balance: {balance} GEL")
        
    elif choice == "3":
        withdraw_amount = int(input("\nEnter amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Successfully withdrawn!")
            print(f"Remaining balance: {balance} GEL")
        else:
            print("Operation denied! Insufficient funds.")
            
    elif choice == "4":
        print(f"\nThank you for using our service, {user_name}!")
        break
        
    else:
        print("\nInvalid choice! Please select 1, 2, 3 or 4.")



     
       
          



