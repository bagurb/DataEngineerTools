import requests
from bs4 import BeautifulSoup

url = "http://www.esiee.fr/"

response = requests.get(url)
soup = BeautifulSoup(response.text)
print(soup)
