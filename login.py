# create a program by python to login to a website
import requests

url = "https://www.google.com"
response = requests.get(url)
print(response.text)

