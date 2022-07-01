
from http.client import HTTPResponse
import re
from unittest import result
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

urls = ['https://threatpost.com/category/vulnerabilities', 'https://news.ycombinator.com']
# links_store = []
for url in urls:
    request = Request(url)
    web_page = urlopen(request)
    soup = BeautifulSoup(web_page, 'html.parser')

    for link in soup.find_all('a', attrs={'href': re.compile("^https://")} ):
        links_store = link.get('href')
        print(link.get('href') + "\n")
  