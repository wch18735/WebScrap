import requests
from bs4 import BeautifulSoup as bf
import os

for year in range(2015, 2020):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()
    soup = bf(res.text, "lxml")

    if not os.path.isdir(f"./images/{year}"):
        os.mkdir(f"./images/{year}")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        else:
            continue
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open(f"./images/{year}/movie{idx+1}.jpg", "wb") as f:
            f.write(image_res.content)