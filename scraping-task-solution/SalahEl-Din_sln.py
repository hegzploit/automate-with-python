#!/usr/bin/python3 

from bs4 import BeautifulSoup
import requests
URL = "https://commits.top/egypt.html"

def get_data(LINK):
    r = requests.get(LINK,"lxml")
    soup = BeautifulSoup(r.content)
    allSpans = soup.find_all("span")
    allImgs = soup.find_all("img")
    for span in allSpans:
        if "p-name" in str(span):
            pName = span
        if "text-bold color-text-primary" in str(span):
            noOfFollowers=span
    for img in allImgs:
        if "avatar" in str(img):
            pImg = img["src"]
    currentName = str(pName.contents).split("\\n")[1]
    noOfFollowers = str(noOfFollowers.contents).strip("[']")
    return currentName,noOfFollowers,pImg

current_URL = URL
r=requests.get(current_URL,"lxml")
soup= BeautifulSoup(r.content) #content => byte string
people_list = soup.find_all("td")
print("Please wait while data is being scraped/stolen")
for i in range(256):
    entry = str(people_list[i])
    if("github.com" in entry):
        entry = entry.split('"')[1]
        name,follow,img = get_data(entry)
        print("Our target:" + name + " has " + follow + " Followers"+ " and his image can be found at: " + img)


    


