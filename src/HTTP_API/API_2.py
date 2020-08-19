import requests, pdb

def play_with_j(s = str(input("Guess\n"))):
    response = requests.get("https://icanhazdadjoke.com/search",
                    headers = {"Accept":"application/json"},
                    params  = {"term":s}
                    )
    if response.json()["total_jokes"] >= 1:
        # pdb.set_trace()
        jokes = list(map(lambda val: f"{val['joke']}", response.json()["results"]))
        return [f"{e}" for e in jokes]
    elif response.json()["total_jokes"] == 0:
        return f"no jokes about {s}"

print(play_with_j())

# or do it shorter with choice

import requests
from random import choice
def play_with_j(m = str(input("Guess\n"))):
    response = requests.get("https://icanhazdadjoke.com/search",
                    headers = {"Accept":"application/json"},
                    params  = {"term":m}
                    )
    total_result = response.json()["total_jokes"]
    total_jokes = response.json()["results"]
    if response:
        print(f"Here are the jokes about {m} : {list(choice(total_jokes['joke']))}")
    elif total_jokes == 0:
        return f"no jokes about {m}"

print(play_with_j())


