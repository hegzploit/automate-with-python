import requests
from bs4 import BeautifulSoup

URL = "https://commits.top/egypt.html"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "lxml")
tds = soup.find_all("td")
clean_tds = []
for td in tds:
    if("br" in str(td)):
        clean_tds.append(td)

for td in clean_tds:
    github_link = str(td.contents[0]["href"])
    name = str(td.contents[-1])
    github_r = requests.get(github_link)
    soup = BeautifulSoup(github_r.content, "lxml")
    followers = soup.find(
        "span", {"class": "text-bold color-text-primary"}).text
    with open("data.csv", "a") as f:
        f.write(f"{github_link}, {name}, {followers}\n")
