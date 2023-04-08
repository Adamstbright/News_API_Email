""" This code uses requests library to access a picture url in a website
    download the image. response.content is used to get binary data such as images.
"""

import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/181px-Cat_August_2010-4.jpg"

response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)


