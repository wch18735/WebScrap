import requests
from bs4 import BeautifulSoup as bf

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = bf(res.text, "lxml") # soup이란 객체로 만듬
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체가 가진 것들 중 첫 번째로 발견되는 a 태그를 가져오기
# print(soup.a.attrs) # attribute 를 확인
# print(soup.a["href"])

# print(soup.find("a", attrs={"class": "Nbtn_upload"})) # find를 이용해 찾아내기
# print(soup.find(attrs={"class": "Nbtn_upload"})) # class 값이 Nbtn_upload 인 element를 찾기
# print(soup.find("li", attrs={"class": "rank01"}))

# next_sibling, previous_sibling, parent, child
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
# print(rank1.a.get_text(), rank2.a.get_text(), rank3.a.get_text())

rank2 = rank1.find_next_sibling("li") # 중간에 해당하는 tag만 찾는 것
print(rank2.a.get_text()) # next_sibling.next_sibling 두 번 안 해도 된다
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

for rank in rank1.find_next_siblings("li"):
    print(rank.a.get_text())

webtoon = soup.find("a", text="참교육-12화") # "a" tag 의 text는 <a> ~ </a> 에 있는 것
print(webtoon)