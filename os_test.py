import os

folder_name = "data_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder {folder_name} made succesfully!")
else:
    print("THis folder already exist")

print('renewed list:', os.listdir())