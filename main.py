from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "D:/ChromeDr/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.instagram.com/accounts/login/")

# user = driver.find_element_by_name("username")
# password = driver.find_element_by_name("password")
# login = driver.find_element_by_class_name("sqdOP")
#
# user.send_keys("")
# password.send_keys("")
# login.click()
#
# time.sleep(5)
# search = driver.find_element_by_class_name("XTCLo")
# search.send_keys("")
#
# time.sleep(3)
# choose = driver.find_element_by_class_name("Igw0E")
# choose.click()
#
# time.sleep(5)
# followers = driver.find_element_by_class_name("-nal3")
# followers.click()
#
# time.sleep(2)
# follow = driver.find_elements_by_class_name("wo9IH")
# for i in follow:
#     i.click()
