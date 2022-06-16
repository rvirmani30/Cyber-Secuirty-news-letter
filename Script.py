import re
from unittest import result
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# 'https://news.ycombinator.com/'
urls = ['https://threatpost.com/category/vulnerabilities/']
links = []
for url in urls:
    request = Request(url)
    web_page = urlopen(request)
    soup = BeautifulSoup(web_page, 'lxml')

    for link in soup.find_all('a'):
        links.append(link.get('href'))
    print(links)