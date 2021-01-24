from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser =  webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 (이번 달)
browser.find_element_by_link_text("가는날 선택").click()
browser.find_elements_by_link_text("27")[0].click()

# 오는 날 선택 (다음 달)
browser.find_elements_by_link_text("28")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 페이지 로딩 처리
try:
    # browser를 10초 동안 기다린다 until XPATH 값에 해당하는 값이 있을 때 까지(By) 기다림
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 첫 번째 결과 출력
    print(elem.text)
finally:
    browser.quit()