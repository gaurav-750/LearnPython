# try:

#     file = open("app.py")

#     age = int(input("Age: "))
#     print("Your age is", age)
#     xfactor = 10/age

#     # file.close()
# except (ValueError, ZeroDivisionError) as err:
#     print("Please enter a valid age!")
#     print(err, type(err))
# else:
#     print("No exception thrown!")
# finally:
#     file.close()  # * FInally clause is always executed

from timeit import timeit
# we can calculate the execution time of python code

code1 = """

def calculate_XFactor(age):
    if age <= 0:
        raise ValueError("Age cannot zero or less!")

    return 10/age


try:
    ans = calculate_XFactor(-1)
    print(ans)
except ValueError as e:
    # print(e)
    pass

"""


code2 = """

def calculate_XFactor(age):
    if age <= 0:
        return None

    return 10/age


ans = calculate_XFactor(-1)
if ans == None:
    pass

"""

print("First Code:", timeit(code1, number=10000))
# this will execute this code 1000 times and calculate the execution time

print("Second Code:", timeit(code2, number=10000))
