# 동적 페이지에대한 selenium
# 구글 무비는 접속하는 Header에 따라 서로 다른 정보를 보여준다

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
user_agent = driver.execute_script("return navigator.userAgent;")
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"
headers = {"User-Aget": user_agent}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
for movie in movies:
    print(movie.get_text())