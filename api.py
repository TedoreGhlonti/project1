
import requests

payload = {"status": "alive", "species": "alien", "page": 2}
res = requests.get("https://rickandmortyapi.com/api/character", params=payload)

data = res.json()
print(f"There are {data['info']['pages']} pages")
print(f"There are {data['info']['count']} counts")



