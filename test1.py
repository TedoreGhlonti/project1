balance = 0

while True:
    print("--- Mobile Balance ---")
    print("1. Show Balance")
    print("2. Add Balance")
    print("3. Log Out")

    choice = int(input('Please make your choice (1/2/3): '))

    if choice == 1:
        print(f'Your Balance is: {balance}')
    elif choice == 2:
        amount = int(input('Please add to balance: '))
        balance += amount
    elif choice == 3:
        print('Goodbye!')
        break
    else:
        print('wrong parameters!')
    
    





    

    
