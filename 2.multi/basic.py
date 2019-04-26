import requests
from bs4 import BeautifulSoup


def spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'http://bcho.tistory.com/' + str(page)
    print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for link in soup.select('h2 > a'):
      href = 'http://bcho.tistory.com/' + link.get('href')
      title = link.string
      print(href)
      print(title)
    page += 1

spider(10)
