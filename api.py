import requests

url = "https://pokeapi.co/api/v2/contest-effect/1/"

res = requests.get(url)

print(res)

data = res.json()


for d in data["effect_entries"]:
    print(d['language'])

new_data = d['language']['url']
print(new_data)








