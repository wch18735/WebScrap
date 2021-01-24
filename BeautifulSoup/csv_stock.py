import requests
from bs4 import BeautifulSoup as bf
import csv

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# title
url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page=1"
res = requests.get(url)
res.raise_for_status()
soup = bf(res.text, "lxml")
keys = [col.get_text() for col in soup.find("thead").find_all("th")]
writer.writerow(keys[:-1])

for page in range(1,5):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?&page={page}"
    res = requests.get(url)
    res.raise_for_status()
    soup = bf(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            # 의미없는 row 삭제
            continue
        data = [column.get_text().strip() for column in columns]
        print(data)
        writer.writerow(data[:-1])

f.close()