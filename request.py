import requests

# ვიყენებთ უფრო სტაბილურ API-ს
url = "https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(url)
    
    # 200 ნიშნავს, რომ ყველაფერი რიგზეა
    if response.status_code == 200:
        data = response.json()
        
        print("--- ცოტა ვიხალისოთ ---")
        print(f"Question: {data['setup']}")
        print(f"Answer: {data['punchline']} 😂")
    else:
        print(f"სერვერმა დააბრუნა შეცდომა: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("შეცდომა: ინტერნეტის კავშირი ვერ დამყარდა! 🌐❌")