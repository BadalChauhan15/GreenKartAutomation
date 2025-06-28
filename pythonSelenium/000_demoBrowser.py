import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Driver Service
service_obj = Service("D:/1/Actual Learning Selenium With Python/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(5)