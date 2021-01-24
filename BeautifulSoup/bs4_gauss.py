import requests
from bs4 import BeautifulSoup as bf

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = bf(res.text, "lxml")

# 만화제목 + 링크
# cartoons = soup.find_all("td", attrs={"class": "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title, "https://comic.naver.com"+link)

# 만화제목 + 링크 화면 전체
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rate = 0
cartoons = soup.find_all("div", attrs="rating_type")
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)
print("전체 점수:", total_rate)
print("평균 점수:", total_rate / len(cartoons))