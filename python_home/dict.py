def say_hello(name):
    return f"Hello {name}"

print(say_hello("Tedore"))

def square(num):
    return num * num

print(square(5))

def find_max(a, b):
    if a > b:
        return a
    else:
        return b
    
print(find_max(10, 5))




def calculate_average(numbers):
    total_sum = 0
    for n in numbers:
        total_sum += n
        
    average = total_sum / len(numbers)
   
    return average



numbers_list = [10, 20, 30, 40]
result = calculate_average(numbers_list)
print(result)

def apply_discount(price, percent):
    new_price = price - (price * percent / 100)
    
    return new_price

print(apply_discount(200, 15))






    

