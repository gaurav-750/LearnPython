import json
from pathlib import Path

movies = [
    {"id": 1, "name": "Terminator", "year": 2010},
    {"id": 2, "name": "Avengers", "year": 2012},
    {"id": 3, "name": "John Wick", "year": 2020},
]


#! Writing into the json file:
json_data = json.dumps(movies)

# creating a json file
jsonFile = Path("movies.json")

# writing data into the json file
# jsonFile.write_text(json_data)

#! Reading from the json file:
jsonData = jsonFile.read_text()
movies = json.loads(jsonData)  # it will convert it into Python object

print(movies)
print(movies[1]["name"])
