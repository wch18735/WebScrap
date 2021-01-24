import requests
from  playsound import playsound
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    # 오늘 기온
    today = soup.find("p", attrs={"class": "cast_txt"}).get_text()
    print(today)

    # 현재 온도
    temperature = soup.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class": "min"}).get_text()
    max_temp = soup.find("span", attrs={"class": "max"}).get_text()
    print(f"현재온도: {temperature} (최저 {min_temp}/최고{max_temp})")

    # 체감 온도
    sensible = soup.find("span", attrs={"class": "sensible"}).get_text().split()
    print(sensible[0]+":", sensible[1])

    # 오전/오후 강수확률
    morning_rain_rate = soup.find("span", attrs={"class": "point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()
    print(f"오전 {morning_rain_rate} | 오후 {afternoon_rain_rate}")

    # 미세먼지
    dust = soup.find("dl", attrs={"class": "indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()
    print(f"미세먼지: {pm10}")
    print(f"초미세먼지: {pm25}")
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)

    news_list = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.div.a.get_text().strip()
        link = url + news.div.a["href"]
        print(f"[{index + 1}]", title, link)
    print()


def scrape_it_news():
    print("[IT 뉴스]")
    for page in range(1,11):
        # 1 ~ 10 page
        url = f"https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=230&sid1=105&date=20210122&page={page}"
        soup = create_soup(url)
        news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li")
        for news in news_list:
            img = news.find("img")
            if img:
                title = news.find_all("a")[1].get_text().strip()
                link = news.find_all("a")[1]["href"]
                print(title, link)
            else:
                title = news.find("a").get_text().strip()
                link = news.find("a")["href"]
                print(title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
    soup = create_soup(url)
    korean_script = soup.find_all("div", attrs={"class": "conv_txt"})[0]
    english_script = soup.find_all("div", attrs={"class": "conv_txt"})[1]

    # 한국어
    print("=" * 10, "한국어", "=" * 10)
    for line in korean_script.find_all("span", attrs={"class": "conv_sub"}):
        print(line.get_text())

    # 영어
    print("=" * 10, "영어", "=" * 10)
    for line in english_script.find_all("span", attrs={"class": "conv_sub"}):
        print(line.get_text())


def scrape_english_news():
    print("[영어 뉴스]")
    url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_engnews_begin&keywd=haceng_submain_lnb_lec_engnews_begin&logger_kw=haceng_submain_lnb_lec_engnews_begin"
    soup = create_soup(url)
    audio_src = soup.find("audio")["src"]
    audio = requests.get(audio_src)
    with open("today_news.mp3", "wb") as f:
        f.write(audio.content)
    script = soup.find("div", attrs={"class": "engnews_article_section"}).get_text()
    print(script)
    playsound("today_news.mp3")

if __name__=="__main__":
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()
    scrape_english_news()