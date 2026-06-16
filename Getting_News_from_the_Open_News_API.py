import requests


url = "https://newsapi.org/v2/everything"

params = {
    "q": "SpaceX",
    "from": "2026-06-15",
    "sortBy": "popularity",
    "apiKey": "54a853140ec14786af0d6c987e967eb6"
    }

response = requests.get(url, params=params)

content = response.json()

articles = content['articles']
print(type(articles))
"""
for article in articles:
    print('TITLE\n',article['title'],\nDESCRIPTION\n',article['description'])
"""

def get_news(topic,from_date,to_date,language='en',api_key='54a853140ec14786af0d6c987e967eb6'):

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "from": from_date,
        "to": to_date,
        "language": language,
        "apiKey": api_key
        }

    response = requests.get(url,params=params)
    content = response.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n{article['title']},'\nDESCRIPTION\n'{article['description']}")
    return results


print(get_news('space',from_date='2026-06-15',to_date='2026-06-16'))
