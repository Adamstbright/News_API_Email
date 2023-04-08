import requests
from send_email import send_email

topic = "tesla"

API_key = "64b6d1be92844673a1ee15a3eb68c0a8"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=64b6d1be92844673a1ee15a3eb68c0a8&" \
      "language=en"

#Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
info = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        info = "subject: Todays news" \
               + "\n" + info + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

info = info.encode("utf-8")
send_email(message=info)


