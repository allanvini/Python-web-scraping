import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

my_url = 'https://g1.globo.com/mundo/'

uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

news = page_soup.findAll("div",{"class":"feed-post-body-title gui-color-primary gui-color-hover"})

newsArr = []

for new in news:
    newsArr.append(
        {
            "title": new.text,
            "link": new.a["href"]
        }
    )

def run():
    output = json.dumps(newsArr)
    with open("news.json","w") as file:
        file.write(output)
run();