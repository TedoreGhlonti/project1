def get_valid_input(prompt, check_type):
    while True:
        user_input = input(prompt).strip()
        
        # ვამოწმებთ რომელი მეთოდი გამოვიყენოთ
        if check_type == "alpha" and user_input.isalpha():
            return user_input
        elif check_type == "digit" and user_input.isdigit():
            return user_input
        elif check_type == "alnum" and user_input.isalnum():
            return user_input
        else:
            print(f"Invalid input! Please follow the rules for {check_type}.")

# ახლა ვიყენებთ ფუნქციას სხვადასხვა მონაცემისთვის:
name = get_valid_input("Enter your name: ", "alpha")
id_code = get_valid_input("Enter your ID: ", "digit")
user_name = get_valid_input("Enter your username: ", "alnum")

print(f"\nSuccess! Welcome {name}. Your ID is {id_code}.")








    
    
    

    



