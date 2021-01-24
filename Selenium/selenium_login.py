from selenium import webdriver
import time
import random

browser = webdriver.Chrome("./chromedriver.exe")

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
login_elem = browser.find_element_by_class_name("link_login")
login_elem.click()

# 3. JavaScript를 이용한 자동 로그인
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id="naver_id", pw="naver_pw")
time.sleep(random.uniform(1, 3)) # 자동화탐지를 우회 하기 위한 delay
browser.execute_script(input_js)
time.sleep(random.uniform(1, 3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()
