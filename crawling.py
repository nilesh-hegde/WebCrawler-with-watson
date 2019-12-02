import ndtv_crawler
import toi_crawler
import api

ndtv_crawler.ndtv_crawl()
toi_crawler.toi_crawl()

try:
    ndtv_file=open("ndtv.txt",'r',encoding="utf-8")
except IOError:
    print("Cannot open NDTV file")

try:
    toi_file=open("toi.txt",'r',encoding="utf-8")
except IOError:
    print("Cannot open TOI file")

i=0
for line in ndtv_file:
    #if i==10:
        #break
    api.analysis(line,'0')
    #i=i+1

i=0
for line in toi_file:
    #if i==10:
        #break
    api.analysis(line,'1')
    #i=i+1

print("Crawling Complete")