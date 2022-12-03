import webbrowser
import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([11, 12, 13, 14, 15]))
print(random.choices([11, 12, 13, 14, 15], k=2))

print(type(string.ascii_letters+string.digits))
print("".join(random.choices(string.ascii_letters+string.digits, k=6)))

nums = [1, 2, 3, 4, 5, 6]
random.shuffle(nums)
print(nums)


print("Task Completed.\nOpening the Web Browser..")
webbrowser.open("https://google.com", new=0)
