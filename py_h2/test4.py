user_time = input("Enter time: ")

new_time = user_time.split(":")

result = int(new_time[0])

if result >= 7 and result <= 9:
    print("Breakfast time!")
elif result >= 12 and result <= 14:
    print("Lunch time!")
elif result >= 18 and result <= 20:
    print("Dinner time!")
else:
    print("Not time to eat!")

print(result)
