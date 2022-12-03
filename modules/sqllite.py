import sqlite3
import json
from pathlib import Path


jsonFile = Path("movies.json")
movies = json.loads(jsonFile.read_text())
# print(movies)


# * Now we have to 'store' this movies into the database:
with sqlite3.connect("db.sqlite32") as connection:
    command = "insert into Movies values(?, ?, ?)"

    for movie in movies:
        # print('movies.values()', movie.values())
        connection.execute(command, tuple(movie.values()))

    connection.commit()


# * Reading form the database:
with sqlite3.connect("db.sqlite32") as conn:
    command = "select * from Movies"
    cursor = conn.execute(command)

    # for row in cursor:
    # print(row)

    movies = cursor.fetchall()
    print(movies)
