prices = [10, 20, 30]

def add_vat(price):
    result = price * 1.18
    return round(result, 2)

def process_prices(price_list):
    new_list = []
    for p in price_list:
       result = add_vat(p) 
       new_list.append(result)
    return new_list

final_prices = process_prices(prices)

print(final_prices)


  




