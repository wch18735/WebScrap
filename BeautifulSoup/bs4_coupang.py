# GET 방식
# ? 뒤에 변수와 값, &를 통해 구분
# 큰 데이터는 입력하지 못 함
# 쉽게 웹 스크래핑 가능!!

# POST 방식 (URL이 그대로 있는 경우)
# 조금 더 보안
# 큰 데이터 입력 가능

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

total = soup.find_all("a", attrs="btn-last disabled")
total = int(total[0].get_text())

for i in range(1, total+1):
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    print("-"*10,f"page{i}","-"*10)

    for item in items:
        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        # 제품 정보 얻음
        name = item.find("div", attrs={"class": "name"}).get_text()
        price = item.find("strong", attrs={"class": "price-value"})
        if price:
            price = price.get_text()
        else:
            continue

        rate = item.find("em", attrs={"class": "rating"})
        if rate:
            rate = rate.get_text()
            rate_cnt = item.find("span", attrs={"class": "rating-total-count"}).get_text()
        else:
            rate = "평점 없음"
            rate_cnt = "평점 수 없음"
            continue

        # Apple 제품 제외
        if "Apple" in name:
            continue

        # 평점 4.5 이상, 리뷰 수 50개 이상
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        if float(rate) >= 4.5 and int(rate_cnt[1:-1]) >= 50:
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate}")
            print("바로가기: {}".format("https://www.coupang.com"+link))
            print("*"*100)
        else:
            continue