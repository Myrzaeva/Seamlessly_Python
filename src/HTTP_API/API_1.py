import requests

response = requests.get("https://icanhazdadjoke.com",
                        headers={"Accept": "application/json"},
                        params={"term":"justin bieber", "limit":1})

data = response.json()
print(f" status: {data}")
