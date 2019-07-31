import requests
import json
import xml.etree.ElementTree as ET

url = 'https://www.infobae.com/feeds/rss/'

response = requests.get(url)

data = ET.fromstring(response.text)

newsArr = []

ns = {'dc': 'http://purl.org/dc/elements/1.1/',
      'content': 'http://purl.org/rss/1.0/modules/content/'}

for news in data.findall('channel/item'):
    newsObject = {
        'title': news.find('title').text,
        'desc': news.find('description').text,
        'pubd': news.find('pubDate').text,
        'author': news.find('dc:creator', ns).text,
        'link': news.find('link').text
    }
    newsArr.append(newsObject)


with open('./datafiles/newsData.json', 'w') as outfile:
    json.dump(newsArr, outfile)

