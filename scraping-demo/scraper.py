import requests
from bs4 import BeautifulSoup

page_URL = "http://books.toscrape.com/catalogue/page-{}.html"
main_URL = "http://books.toscrape.com"

for i in range(50):
    current_URL = page_URL.format(i+1)
    r = requests.get(current_URL)
    soup = BeautifulSoup(r.content, "lxml")
    imgs_list = soup.find_all("img")
    for img_tag in imgs_list:
        img_link = main_URL + img_tag["src"][2:]
        img_text = img_tag["alt"]
        with open(f"{img_text}.jpg", "wb") as img:
            img.write(requests.get(img_link).content)
