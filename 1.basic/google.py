import requests
from bs4 import BeautifulSoup

def getpage(url):
  resp = requests.get(url)
  print(resp.text)

url = 'https://www.google.com'
getpage(url)
