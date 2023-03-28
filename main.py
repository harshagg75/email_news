import requests

api_key = "dc1a3384a95a460388be9df2233239b5"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-28&sortBy" \
      "=publishedAt&apiKey=dc1a3384a95a460388be9df2233239b5"

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])