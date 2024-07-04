from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.pornhub.com/video?o=mv&t=a&cc=world&page={n}"
page = urlopen(url.format(n=1))
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print(soup)