import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url = 'https://www.infobae.com/feeds/rss/'

response = requests.get(url)

data = ET.fromstring(response.text)

for news in data.findall('channel/item'):
    title = news.find('title').text
    desc = news.find('description').text

    print(title)
    print(desc)
    print()
