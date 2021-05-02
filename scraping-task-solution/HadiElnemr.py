#!usr/bin/python3
import requests
import re
import csv
from bs4 import BeautifulSoup as sp

USERSCNT = 256
COLSCNT = 4

main_url = "https://commits.top/egypt.html"
r = requests.get(main_url)
soup = sp(r.content, 'html.parser')
table = soup.findAll('td')

with open('test1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(USERSCNT*COLSCNT + 1):
        if i % COLSCNT == 1:  # get 2nd column
            try:
                row = table[i].contents
                username = row[0].text
                prof = 'https://github.com/' + username
                r = requests.get(prof)
                soup = sp(r.content, 'html.parser')
                name_tag = soup.find(
                    'span', {"class": "p-name vcard-fullname d-block overflow-hidden"}).contents
                name = name_tag[0].strip()
                followers_tag = soup.find(
                    'span', {"class": "text-bold color-text-primary"}).contents
                followers = followers_tag[0]
                user_info = [prof, name, followers]
                writer.writerow(user_info)
            except:
                print("error, closing file")
