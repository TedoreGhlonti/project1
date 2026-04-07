import sys
import requests

# 1. ვამოწმებთ, შეიყვანა თუ არა მომხმარებელმა რაოდენობა
if len(sys.argv) < 2:
    sys.exit("გთხოვთ, მიუთითოთ პოსტების რაოდენობა! (მაგ: python script.py 3)")

try:
    # 2. გადაგვაქვს არგუმენტი მთელ რიცხვში (int)
    limit = int(sys.argv[1])
    
    # 3. მოგვაქვს ყველა პოსტი
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    res.raise_for_status()
    
    data = res.json()
    
    # 4. ვიყენებთ Slicing-ს სიის დასამოკლებად [:limit]
    limited_data = data[:limit]
    
    print(f"--- პირველი {limit} პოსტის სათაურები ---")
    
    # 5. ციკლით ვბეჭდავთ სათაურებს
    for post in limited_data:
        print(f"📌 {post['title']}")

except ValueError:
    sys.exit("შეცდომა: გთხოვთ, შეიყვანოთ მხოლოდ ციფრები!")
except requests.exceptions.HTTPError:
    sys.exit("ვერ მოხერხდა მონაცემების წამოღება სერვერიდან.")






 