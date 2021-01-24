import requests
from bs4 import BeautifulSoup as bf

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# 네이버 웹툰 전체 목록 가져오기
soup = bf(res.text, "lxml") # soup이란 객체로 만듬
cartoons = soup.find_all("a", attrs={"class": "title"}) 
# soup 객체 전체에서 tag 명이 a 이고 class 명이 title인 모든 element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())