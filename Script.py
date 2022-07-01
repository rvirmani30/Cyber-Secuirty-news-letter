from http.client import HTTPResponse
import re
from unittest import result
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import schedule
import time


def script():
    urls = ['https://threatpost.com/category/vulnerabilities', 'https://news.ycombinator.com']
    # links_store = []
    for url in urls:
        request = Request(url)
        web_page = urlopen(request)
        soup = BeautifulSoup(web_page, 'html.parser')

        for link in soup.find_all('a', attrs={'href': re.compile("^https://")} ):
            links_store = link.get('href')
            print(link.get('href') + "\n")

def scheduling_script():
    print ("Scedule script ran")
    schedule.every(1).day.at("18:53").do(script)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    scheduling_script()
