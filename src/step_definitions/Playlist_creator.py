playlist = {
    "title": "chase",
    "author": "colt steela",
    "songs": [
        {"title": "chase",
         "artist": ["sober"],
         "duration": 2.5},
        {"title": "passion",
         "artist": ["sevish", "dj_calid"],
         "duration": 5.5},
        {"title": "winter",
         "artist": ["hot'n'fun"],
         "duration": 3}
    ]
}
print(playlist["songs"])

for x in playlist["songs"]:
    print(x["title"])

music_length =0
for i in playlist["songs"]:
    music_length += i["duration"]
print(music_length)


empty_dictionary =[]
print(empty_dictionary)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[e]: list2[e] for e in range(0, len(list1))}
print(answer)
#or by using zip()
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

dict(zip(list1, list2))
