import json
movie= {
    "title":"a",
    "year": "2000",
    "actor":{"leading":"a","supporting":"b"},
    "oscar": True,
    "genre":"1"
}

file = open("favourite.json", "w")

json.dump(movie, file, indent = 6)

file.close()

"""

with open("favourite.json", "w", encoding = "utf8") as file:
    json.dump(movie, file, indent = 4)
file.close()
"""