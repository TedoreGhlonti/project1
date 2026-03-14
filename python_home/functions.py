def get_valid_age():
    while True:
        user_input = input("გთხოვთ შეიყვანოთ თქვენი ასაკი: ")
        
        if user_input.isdigit():
            age = int(user_input)
            if 0 <= age <= 120:
                return age  
            else:
                print("შეცდომა: ასაკი უნდა იყოს 0-დან 120-მდე!")
        else:
            print("შეცდომა: გთხოვთ შეიყვანოთ მხოლოდ ციფრები!")

def calculate_price(age):
    if age < 18:
        return "ფასი: 10 ლარი"
    elif age >= 65:
        return "ფასი: 5 ლარი"
    else:
        return "ფასი: 20 ლარი"

my_age = get_valid_age()

final_price = calculate_price(my_age)

print(f"თქვენი ასაკია {my_age}, შესაბამისად {final_price}")



