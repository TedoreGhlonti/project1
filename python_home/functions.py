# 1. პატარა ფუნქცია: უმატებს 5-ს
def add_five(n):
    return n + 5

# 2. მთავარი ფუნქცია: აორმაგებს იმას, რასაც მიიღებს
def double_number(number):
    # აქ ვიძახებთ პირველ ფუნქციას! 
    # ჯერ ემატება 5, მერე მრავლდება 2-ზე
    result = add_five(number) * 2
    return result

# გამოძახება
final_val = double_number(10)
print(final_val) # დაბეჭდავს 30-ს (რადგან (10+5) * 2 = 30)