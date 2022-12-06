import requests
import config

url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/info"

headers = {
    "X-RapidAPI-Key": config.api_key,
    "X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
