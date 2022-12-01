# age = 20
# print(type(age))
# print('age 20', id(age))

# age = 11
# print('age 11', id(age))


# list = [1, 2, 3]
# print('list', id(list))

# list.append(4)
# print('list after append:', id(list))

# course: str = "Python Course"
# print(len(course))

# print(course[0:3])

# str = "Python \"Program"
# print(str)


# msg = """ Python
#     kya bolti jaanta
#     kaisi hai..
# """

# print(msg)

# first = "Gaurav"
# last = "Somani"
# full = f"{len(first)} {last}"
# print(full)


# course = "Python Program"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find("ho"))
# print(course.replace("P", "-"))

# print("ho" in course)

# * Numbers
# x = 0b10
# print(bin(x))


# print(10/3)
# print(10//3)

import math

# PI = 3.14
# print(round(PI))
# print(abs(PI))

# print(math.floor(PI))
# print(math.ceil(PI))

# x = int(input("x: "))
# y = x+1
# print('y', y)

# print(bool(x))


# age = 22
# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# print("All done!")


# age = 22
# if 18 <= age < 65:
#     print("You are eligible!")

# msg = "Eligible" if age >= 18 else "Nahane jaa"
# print(msg)

# for x in "Python":
#     print('x', x)


# for name in ['gadfjs', 'sbvjsygf']:
#     print(name)

# for num in range(0, 10, 2):
#     print('num', num)

# print(type(range(5)))


# names = ["gJohn", "Mary"]

# for name in names:
#     if name.startswith("J"):
#         print("Found J!")
#         break
# else:
#     print("Not found J!")

# guess = 0
# ans = 5

# while guess != ans:
#     guess = int(input("Guess: "))


# for num in range(0, 5):
#     if num == 3:
#         break
#     print('num', num)
# else:
#     print('inside else')


# def increment(num, by) -> tuple:
#     updatednum = num + by
#     return num, updatednum


# print(increment(2, 3))

# def multiply(*list):
#     ans = 1
#     for num in list:
#         ans = ans*num
#     return ans


# print('ans', multiply(4, 5, 3, 4, 5))


# def saveUser(**user):
#     print('user', user["name"])


# saveUser(id=1, name="Admin")


# def greet():
#     if True:
#         message = "Hello there"

#     print('The mesaage is', message)


# greet()

# def multiply(*nums):
#     product = 1
#     for num in nums:
#         product *= num

#     return product

# print("Start")
# print(multiply(1, 2, 3))
# print("Finish")


def FizzBuzz(num):
    output = ""
    if (num % 3 == 0 and num % 5 == 0):
        output = "FizzBuzz"
    elif (num % 3 == 0):
        output = "Fizz"
    elif (num % 5 == 0):
        output = "Buzz"
    else:
        output = num

    return output


print(FizzBuzz(7))


myMovies = [
    {"imdb": 9, "rating": 4.6},
    {"imdb": 8.5, "rating": 4.2},
    {"imdb": 8, "rating": 4}
]


def imdbs(item):
    return item["imdb"]


imdbRatings = map(imdbs, myMovies)
print('imdbs:', list(imdbRatings))
