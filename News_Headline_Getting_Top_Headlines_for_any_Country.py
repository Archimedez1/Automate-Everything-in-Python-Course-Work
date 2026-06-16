import requests



def get_news(country,api_key='54a853140ec14786af0d6c987e967eb6'):

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key
        }

    response = requests.get(url,params=params)
    content = response.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n{article['title']},'\nDESCRIPTION\n'{article['description']}")
    return results


print(get_news(country='us'))
