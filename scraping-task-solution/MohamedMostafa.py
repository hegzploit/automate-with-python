import requests
from bs4 import BeautifulSoup
import re

main_URL="https://commits.top/egypt.html"
page_URL="https://github.com/{}"

r=requests.get(main_URL)
soup=BeautifulSoup(r.content,"lxml")
users=soup.find_all("a",href=re.compile("^https://github.com/"))
users_list=[]
for item in users[2:258] :
    link=item["href"]
    name=item.string
    #user1=["Name : "+" "+ str(name) ,"His Link : "+" "+ str(link) ]
    #users_list.append(user1)
    profile=page_URL.format(str(name))
    profile_info=requests.get(profile)
    profile_soup=BeautifulSoup(profile_info.content,"lxml")
    followers_num=profile_soup.find_all("span", class_=re.compile("^text-bold color-text-primary"))[0].string
    with open("users.csv","a") as users :
        users.write(f"{name},{link},{followers_num}\n")