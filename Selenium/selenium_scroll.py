# 동적 페이지에대한 selenium
# 구글 무비는 접속하는 Header에 따라 서로 다른 정보를 보여준다

from selenium import webdriver

url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
browser.get(url)

# 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 지정한 위치까지 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
    
# 스크래핑 작업
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, ": <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a")["href"]
    link = "https://play.google.com" + link

    print("=" * 100)
    print(f"제목: {title}")
    print(f"할인 전 가격: {original_price}")
    print(f"할인 후 가격: {price}")
    print(f"링크: {link}")
