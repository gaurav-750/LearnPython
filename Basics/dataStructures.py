from queue import Queue
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque

# mylist = [12, 2, "goodday"]
# mat = [[2, 3], [1, 2]]

# zeroes = [0]*10
# # print(zeroes)

# nums = list(range(0, 20))
# print(nums)

# chars = list("Hello World")
# print(chars)


letters = ["a", 'b', 'c']
# print(letters[0:2])
# print(letters[::-1])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-2])

# first, second, *other = nums
# print(first, second, other)

# for index, letter in enumerate(letters):
#     print(index, letter)

# * Add
# letters.append("Gaurav")
# letters.insert(2, "Hehe")

# print(letters)

# # * Remove
# letters.pop()
# letters.remove("Hehe")
# print(letters)

# del letters[0:2]
# print(letters)

# letters.clear()
# print(letters)

# * Find:
# print(letters.index("c"))


# nums = [4, 2, 1, 1, 45, 21]
# nums.sort(reverse=True)
# sortedNums = sorted(nums, reverse=True)
# print(sortedNums)


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 1),

]


# items.sort()  // this wont directly sort the items
# print(items)


# * You need to define a function for sorting
def sortItems(item):
    return item[1]


items.sort(key=lambda item: item[1])
# print(items)


movies = [
    {
        "name": "A",
        "rating": 3.5
    },
    {
        "name": "B",
        "rating": 4.5
    },
    {
        "name": "A",
        "rating": 4
    }
]


def sort_data(obj):
    return obj["rating"]


movies.sort(key=sort_data, reverse=True)
# print(movies)

ratings = map(lambda item: item["rating"], movies)
# print(ratings) => a map object
ratingsList = list(ratings)  # convert it into a list

# print('ratings list', ratingsList)


def filter_movies(data):
    return data["rating"] >= 4


filtered = filter(filter_movies, movies)
filteredList = list(filtered)

# print('filtered', filteredList)

list1 = [{
    "name": "A",
    "rating": 4
}, 2, 3, 4, 5, 6, 7]
list2 = [11, 12, 13, 14, 15]

tupleList = list(zip("Gaurav", list1, list2))
# print(tupleList)


# ! Stacks
browsingSession = []
browsingSession.append(1)
browsingSession.append(2)
browsingSession.append(3)

# print(browsingSession)

last = browsingSession.pop()
# print(last)

# * to get the last (i.e top of the Stack)
# print('redirect', browsingSession[-1])

# if not browsingSession:
#     print("empty")
# else:
#     print("Not Empty")
#     print('top', browsingSession[-1])

# print(len(browsingSession))


queue: "deque" = deque([])
print('queue initially:', queue)

queue.append(1)
queue.append(2)
queue.append(3)

print("after inserting:", queue)

queue.popleft()
print("removed first element:", queue)

queue.append("Gaurav")
print(queue)

while len(queue) != 0:
    print(queue.popleft())


#! Tuple
# point = ((1, 2, 5, 4))
# print(type(point))
# print(point)


# x = 10
# y = 11

# # ? Swapping
# x, y = y, x
# print('x', x, ' y', y)

# a, b = 1, 2
# print(a, b)

#! Array
# arr = array("i", [1, 2, 3, 4, 5])
# arr.insert(2, 99)
# print('first elemnt', arr[0])
# print(arr)


#! Sets:
uniqueItems = {1, 2, 3, 4, 3, 5, 5}
print(uniqueItems)

nums = [1, 2, 3, 4, 4, 5, 6, 7, 7]
uniqueNums = set(nums)
print('Unique Numbers', uniqueNums)

uniqueNums.add(11)
uniqueNums.remove(7)
print(uniqueNums, len(uniqueNums))


second = {3, 12}

# *Union
print(uniqueNums | second)

# *Intersection
print(uniqueNums & second)

# *Difference
print(uniqueNums - second)

# * Get the items which are not in both the sets: Union - Intersection
print(uniqueNums ^ second)


#! Dictionaries:
# point = {
#     "x": 1,
#     "y": 2,
# }

map = dict(x=1, y=2)
map["z"] = 20
print(map)

# to get the value of a key
print(map["x"])

val = map.get("z")
print('val', val)

# loop over a HashMap (Dictionary)
for key in map:
    print(key, map.get(key))

for key, val in map.items():
    print(key, val)

# Delete
del map["x"]
print(map)


# List Comprehension

# * Syntax
# list = [expression for item in items]
numList = []
# for x in range(0, 5):
#     numList.append(x*2)

# print(numList)

# Same can be done with Comprehension;
numList = [(x*2) for x in range(0, 5)]
print(numList)

# * For sets
numSet = {x*2 for x in range(0, 5)}
print(numSet)

# * For Dictionaries
numsMap = {}
# for x in range(0, 5):
#     numsMap[x] = x*2
# print(numsMap)

numsMap = {x: x*2 for x in range(0, 5000)}
print('HashMap:', getsizeof(numsMap))

# Tuple:
numTuple = (x*2 for x in range(0, 5000))
print('Tuple', numTuple)
print(getsizeof(numTuple))


numbers = [1, 2, 3, 4]
print(numbers)
print(*numbers)

values = [*range(0, 5), *"Hello"]
print(values)


map1 = dict(x=11, y=12)
map2 = dict(x=99)

combined = {**map1, **map2}
print('combined', combined)


# todo Exercise: Find the most repeated character
sentence = "This is a common interview question"

sentence = sentence.replace(' ', "")
map = dict()

for letter in sentence:
    if letter in map:
        val1 = map[letter]
        map[letter] = val1+1
    else:
        map[letter] = 1


def sortMap(item):
    return item[1]


# Sorting the map according to frequency in reverse order
frequencies = sorted(map.items(), key=sortMap, reverse=True)

pprint(frequencies)
mostRepChar = frequencies[0]
print('Most Repeated Character', mostRepChar)

# cnt = 0
# mostRepChar = ''

# for key in map:
#     if map[key] > cnt:
#         cnt = map[key]
#         mostRepChar = key

greet = "Hello"
for ele in enumerate(greet, start=10):
    print('ele:', ele)

myList = [1, 3, 5, 7, 9, 11]
indx = myList.index(5)
print(indx)

myMovies = [
    {"imdb": 9, "rating": 4.6},
    {"imdb": 8.5, "rating": 4.2},
    {"imdb": 8, "rating": 4}
]


def sort_mydata(movie):
    return movie["imdb"]


# myMovies.sort(key=sort_mydata)
sortedMovies = sorted(myMovies, key=sort_mydata)
print("After sorting my movies:", sortedMovies)

myNums = [3, 45, 5, 2, 1, 2]
myNums.sort(reverse=True)
print(myNums)


myStack: deque[str] = deque()
myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)

top = myStack.pop()
print('top', top)

print(myStack)


# q = []
# q.append(11)
# q.append(21)
# q.append(31)
# print('Intitial Queue:', q)
# removedItem = q.pop(0)
# print('item removed', removedItem)
# print(q)


queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)

print('queue:', list(queue))
queue.popleft()
print('queue:', queue)


q2: Queue[int] = Queue(maxsize=-1)
q2.put(100)
q2.put(200)
q2.put(300)

print(q2)
print(q2.qsize())
print(q2.full())

print(q2.get())
print(q2)


myTuple = (1, 3, 4, 5, 6, 9)
print(myTuple)
print(myTuple[1:])
print(myTuple[::2])

team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

print(type(team))

team1 = dict([
    ('Colorado', 'Rockies'),
    ('Colorado', 'Rockies'),
    ('Colorado', 'Rockies'),
    ('xxx', 'xxx'),
])
print(type(team1))

team["CSK"] = "Dhoni"
pprint(team)

for key in team:
    print('key', key)

for x, y in team.items():
    print(x, y)


listx = [1, 2, 3, "Gaurav", "Somani"]
f, s, *t = listx
print(f, s, t)

res = {**team, **team1}
pprint(res)


g = 10
if g > 5:
    raise Exception('Value of x cannot be > 5. The value was', g)
