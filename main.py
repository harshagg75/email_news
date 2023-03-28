import requests
from send_email import send_mail

api_key = "dc1a3384a95a460388be9df2233239b5"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-28&sortBy" \
      "=publishedAt&apiKey=dc1a3384a95a460388be9df2233239b5"

request = requests.get(url)

content = request.json()
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" +article["description"] + 2*"\n"



body = body.encode("utf-8")
send_mail(message=body)