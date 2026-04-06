def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "შეცდომა: ნულზე გაყოფა არ შეიძლება!"
    except TypeError:
        return "შეცდომა: გთხოვთ მიაწოდოთ მხოლოდ რიცხვები და არა ტექსტი!"

print(divide_numbers(15, 5)) # ახლა ესეც აღარ "გააფუჭებს" პროგრამას
    





