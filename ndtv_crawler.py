import requests
from bs4 import BeautifulSoup


def ndtv_crawl():
    url='https://www.ndtv.com/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    file=open("ndtv.txt",'w',encoding="utf-8")
    for link in soup.findAll('a',{'class':'item-title'}):
        if link.string==None:
            continue
        file.write(link.string)
        file.write("\n")
