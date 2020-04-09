from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import os

html_page = urllib.request.urlopen("https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases")
base_url = 'https://data.humdata.org/'
soup = BeautifulSoup(html_page)
pattern = r'([A-Za-z0-9_\./\\-]*).csv'


filenames = []

for file_name in soup.findAll('a', attrs={'title': re.compile(".csv")}):
    if type(str(file_name)) is not None:
        message = re.search(pattern, str(file_name))
        filenames.append(str(message.group()))

# print(repr(filenames))
counter = 0
for link in soup.findAll('a', attrs={'href': re.compile(".csv")}):
    with urllib.request.urlopen(base_url + link.get('href')) as testfile, open(filenames[counter], 'w') as f:
        f.write(testfile.read().decode())
    counter += 1