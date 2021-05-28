from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "D:/ChromeDr/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
cps = driver.find_element_by_id("cps")
timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:

        print(cps.text)
        timeout = time.time() + 5


