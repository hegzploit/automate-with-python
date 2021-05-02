import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup


gucians = []
page_URL = 'https://commits.top/egypt.html'
r = requests.get(page_URL)
soup = BeautifulSoup(r.content, "html.parser")
developers = soup.select(".users-list a")
cache_dir = ".dev-cache"


print("Scrapping, keep your patience!!!")
print("--------------------------------")


if os.path.isfile(cache_dir):
    os.remove(cache_dir)
if not os.path.isdir(cache_dir):
    os.mkdir(cache_dir)


for dev in tqdm(developers):
    URL = dev["href"]
    _ = URL.split("/")
    username = _[len(_) - 1]
    cache_file = os.path.join(cache_dir, username)

    if os.path.isfile(cache_file):
        file = open(cache_file, 'r')
        HTML = file.read()
        file.close()
    else:
        HTML = requests.get(URL).content
        file = open(cache_file, 'wb')
        file.write(HTML)
        file.close()

    dev_soup = BeautifulSoup(HTML, "html.parser")
    bio = dev_soup.select(".user-profile-bio")
    work_for = dev_soup.select("[itemprop=worksFor]")
    work_for = work_for[0].text if len(work_for) > 0 else ""
    to_search_in = work_for + (bio[0].text.lower() if len(bio) > 0 else "")
    to_search_in = to_search_in.lower()

    if ("guc" in to_search_in or "german" in to_search_in):
        name = dev_soup.select(".vcard-fullname")[0].text
        more_info = dev_soup.select(".js-profile-editable-area .Link--secondary")
        followers = more_info[0].find("span").text
        following = more_info[1].find("span").text
        gucians.append((username, name.strip(), followers, following, URL))


print("Writing to ./gucians.csv")
print("--------------------------------")


with open("gucians.csv", "w") as f:
    f.write("username,name,followers,following,url\n")
    for dev in gucians:
        f.write(f"{dev[0]},{dev[1]},{dev[2]},{dev[3]},{dev[4]}\n")

