#!/usr/bin/python3
import csv
from bs4 import BeautifulSoup
import requests
URL = "https://commits.top/egypt.html"
NUMBER_OF_PEOPLE=256
def get_data(LINK):
    r = requests.get(LINK)
    soup = BeautifulSoup(r.content,"lxml")
    all_spans = soup.find_all("span")
    all_imgs = soup.find_all("img")
    for span in all_spans:
        if "p-name" in str(span):
            person_name = span
        if "text-bold color-text-primary" in str(span):
            no_of_followers = span
    for img in all_imgs:
        if "avatar" in str(img):
            person_img = img["src"]
    current_name = str(person_name.contents).split("\\n")[1]
    no_of_followers = str(no_of_followers.contents).strip("[']")
    return current_name, no_of_followers, person_img


current_URL = URL
r = requests.get(current_URL)
soup = BeautifulSoup(r.content,"lxml")
people_list = soup.find_all("td")
print("Please wait while data is being scraped/stolen")
for i in range(NUMBER_OF_PEOPLE):
    entry = str(people_list[i])
    if("github.com" in entry):
        entry = entry.split('"')[1]
        name, follow, img = get_data(entry)
        row=[name,follow,img]
        with open('data.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow(row)

