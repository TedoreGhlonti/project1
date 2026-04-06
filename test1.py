balance = 0
history = [] 

while True:
    print("\n--- Mobile Balance ---")
    print("1. Show Balance")
    print("2. Add Balance")
    print("3. Transaction History")
    print("4. Log Out")

    choice = input('Please make your choice (1/2/3/4): ')

    if choice == "1":
        print(f'Your Balance is: {balance} GEL')
    elif choice == "2":
        amount = int(input('Please add to balance: '))
        balance += amount
        history.append(f"Added: {amount} GEL") 
        print(f"Success! Current balance: {balance} GEL")
    elif choice == "3":
        print("\n--- History ---")
        if not history:
            print("No transactions yet.")
        for item in history:
            print(item)
    elif choice == "4":
        print('Goodbye!')
        break
    else:
        print('Wrong parameters!')
    
    





    

    
