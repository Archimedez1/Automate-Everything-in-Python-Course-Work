import requests

url = "https://newsapi.org/v2/everything"

params = {
    "q": "SpaceX",
    "from": "2026-06-15",
    "sortBy": "popularity",
    "apiKey": "54a853140ec14786af0d6c987e967eb6"
}

r = requests.get(url, params=params)
content = r.json()

print(content['articles'][0]['description'])

