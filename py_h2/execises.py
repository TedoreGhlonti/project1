user_name = input("Please enter your name: ").strip().capitalize()
balance = 500

while True:
    print("\n" + "="*20)
    print("      ATM MENU")
    print("="*20)
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Exit")
    
    choice = input("\nPlease choose an option (1-3): ")
    if choice == "1":
        print(f"\nAccount Holder: {user_name}")
        print(f"Current Balance: {balance} GEL")
        
    elif choice == "2":
        withdraw_amount = int(input("\nEnter amount to withdraw: "))
        
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Successfully withdrawn!")
            print(f"Remaining balance: {balance} GEL")
        else:
            print("Operation denied! Insufficient funds.")
            
    elif choice == "3":
        print(f"\nThank you for using our service, {user_name}! Goodbye.")
        break
        
    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")



     
       
          



