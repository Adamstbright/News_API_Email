import requests
from send_email import send_email

API_key = "64b6d1be92844673a1ee15a3eb68c0a8"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-03-06&sortBy=publishedAt&apiKey=64b6d1be9284467" \
      "3a1ee15a3eb68c0a8"

#Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
info = ""
for article in content["articles"]:
    if article["title"] is not None:
        info = info + article["title"] + "\n" + article["description"]

    info = info.encode("utf-8")
    send_email(message=info)


