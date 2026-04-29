import os 


folder = "products"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder {folder} created!")
else:
    print(f"Folder {folder} already exist!")

item = input("What product? ")
count = input("How many? ")

with open("products/products.txt", "a") as f:
    f.write(f"{item}: {count}\n")

print("___ current products list ___")
with open("products/products.txt", "r") as f:
    for line in f:
        print(line.rstrip())