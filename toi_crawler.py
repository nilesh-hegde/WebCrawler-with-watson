import requests
from bs4 import BeautifulSoup

def toi_crawl():
    url='https://timesofindia.indiatimes.com/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    file=open("toi.txt",'w',encoding="utf-8")
    for link in soup.findAll('div',{'class':'top-story'}):
        for link2 in link.findAll('a'):
            headline = link2.get('title')
            if headline==None:
                continue
            file.write(headline)
            file.write("\n")
    for link in soup.findAll('div',{'class':'widget'}):
        for link2 in link.findAll('a'):
            headline = link2.get('title')
            if headline==None:
                continue
            file.write(headline)
            file.write("\n")
    
