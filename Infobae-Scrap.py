import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url = 'https://www.infobae.com/feeds/rss/'

urllib.request.urlretrieve(url, './datafiles/data.xml')

e = ET.parse('./datafiles/data.xml')

root = e.getroot()

for news in root.findall('channel/item'):
    title = news.find('title').text
    desc = news.find('description').text

    print(title)
    print(desc)
    print()
