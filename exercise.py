numbers = [10, 27, 33, 44, 54]
i = 0
new_list = []

while i < len(numbers):
    if numbers[i] % 2 != 0:
        new_list.append(numbers[i])

    i += 1

print(new_list)



