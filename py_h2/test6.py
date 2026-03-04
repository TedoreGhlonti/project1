def count_evens(numbers_list):
    count = 0
    for n in numbers_list:
        if n % 2 == 0:
            count += 1
            
            
    return count
        

my_list = [1, 2, 3, 4, 5, 6]
result = count_evens(my_list)
print(f"In list is {result} number")

         
        
