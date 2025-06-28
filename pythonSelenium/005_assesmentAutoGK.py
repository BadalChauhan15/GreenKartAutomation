import time

from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ser = Service("D:/1/Actual Learning Selenium With Python/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# for find_elements returning list, implicit wait will not work. It is the only exceptional case.
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # it will provide list[]
count = len(results)

assert count > 0
expected_products = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_products = []
for result in results:
    # chaining of web elements (parent-to-child) to construct dynamically
    actual_products.append(result.find_element(By.XPATH, "h4").text)

assert actual_products == expected_products, \
    f"Products are not matching \nExpected Products: {expected_products} \nActual Products: {actual_products}"
print("Expected Products: "+str(expected_products)+"\nActual Products: "+str(actual_products))