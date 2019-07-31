import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

all_tags = soup.findAll('a')

for i in range(36, len(all_tags)+1):

    one_tag = all_tags[i]

    link = one_tag['href']

    download_url = 'http://web.mta.info/developers/' + link

    urllib.request.urlretrieve(download_url, './datafiles/' + link[link.find('/turnstile_')+1:])

    time.sleep(1)

