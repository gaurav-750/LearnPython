import requests
from bs4 import BeautifulSoup

# get the web page
response = requests.get("https://stackoverflow.com/questions")
# print('response', response)
# print('response.text', response.text)

soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")

print(type(questions[0]))
print(questions[0].attrs)
i = 1

for question in questions:
    print(i, ".", question.select_one(".s-link").get_text())
    print(question.select_one(".s-post-summary--stats-item-number").get_text())
    i += 1
