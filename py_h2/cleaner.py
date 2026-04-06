import os
import shutil

# 1. მიუთითე შენი "სავარჯიშო" საქაღალდის გზა
# ყურადღება: შეცვალე 'C:/Users/User/Desktop/Test_Folder' შენი რეალური გზით
folder_path = 'D:\Minsk memories'

# 2. შევქმნათ სამიზნე საქაღალდეების სახელები
images_dir = os.path.join(folder_path, 'Images')
video_dir = os.path.join(folder_path, 'Videos')

# 3. შევქმნათ ეს საქაღალდეები, თუ ისინი ჯერ არ არსებობს
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print("შეიქმნა საქაღალდე: Images")

if not os.path.exists(video_dir):
    os.makedirs(video_dir)
    print("შეიქმნა საქაღალდე: Videos")

# 4. გადავუაროთ ფაილებს სათითაოდ
for filename in os.listdir(folder_path):
    # სრული გზა ფაილამდე
    file_path = os.path.join(folder_path, filename)

    # შევამოწმოთ, რომ ეს ნამდვილად ფაილია და არა საქაღალდე
    if os.path.isfile(file_path):
        
        # თუ სურათია
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.gif')):
            shutil.move(file_path, os.path.join(images_dir, filename))
            print(f"გადავიტანე სურათი: {filename}")
            
        # თუ დოკუმენტია
        elif filename.lower().endswith(('.mp4',)):
            shutil.move(file_path, os.path.join(video_dir, filename))
            print(f"გადავიტანე დოკუმენტი: {filename}")

print("--- დახარისხება დასრულდა! ---")