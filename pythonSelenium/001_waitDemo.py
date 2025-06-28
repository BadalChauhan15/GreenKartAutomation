import time

from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome locators
from selenium.webdriver.common.by import By

ser = Service("D:/1/Actual Learning Selenium With Python/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # it will provide list[]
count = len(results)

assert count > 0
for result in results:
    # chaining of web elements (parent-to-child) to construct dynamically
    result.find_element(By.XPATH, "div/button").click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(5)

verify = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

assert verify == "Code applied ..!"
print(verify)