import time

from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome locators
from selenium.webdriver.common.by import By

ser = Service("D:/1/Actual Learning Selenium With Python/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# for find_elements returning list, implicit wait will not work. It is the only exceptional case.
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # it will provide list[]
count = len(results)

assert count > 0
for result in results:
    # chaining of web elements (parent-to-child) to construct dynamically
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
verify = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

assert verify == "Code applied ..!"
print(verify)