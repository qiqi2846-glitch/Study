#%% - Import Lib
import requests as rq
from bs4 import BeautifulSoup as bs

#%% - Crawl data from Url
url = "https://tuoitre.vn/lan-song-sa-thai-am-tham-tang-cao-dip-cuoi-nam-20250124100524156.htm"
response = rq.get(url)

#%% - Display data
if response.status_code == 200:
    returned_data = response.text
    #print(returned_data)
    soup = bs(returned_data, "html.parser")

    #title = soup.find("title").text
    #print(title)

    #sub_title = soup.find("h2", class_="detail-sapo").text
    #sub_title = soup.find("h2", {"class": "detail-sapo"}).text
    #print(sub_title)

    comment = soup.find("span", {"class": "contentcomment"}).text
    print(comment)