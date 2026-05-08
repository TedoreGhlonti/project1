import requests

url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url)

data = res.json()

for user in data:
    print(f"{user['name']} works at {user['company']['name']}\n"
          f"Website: {user['website']}"
          )
    
    print("-" * 30)
    



    
