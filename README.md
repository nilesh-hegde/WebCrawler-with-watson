# Webcrawler and Tone Analytics using IBM Watson

The given scrapes data(Headlines) from leading news sites like Times of India, NDTV and so on. The scraped data is then sent to IBM Watson API to perfom tone analytics. The analytics score for each data is stored in an Sqlite DataBase and this data is then visualised. The static HTML Page then displays the results.


NOTE:
1. IBM Watson account has to be created and the credentials should be used in 'api.py'.
2. The 'toi_crawler' and 'ndtv_crawler' files need to be updated as and when required manually since the website keeps changing its webpages.
