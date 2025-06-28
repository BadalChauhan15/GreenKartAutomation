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
for result in results:
    # chaining of web elements (parent-to-child) to construct dynamically
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# our application will take 2 seconds for each element to load,
# but if our one element needs more seconds for it to load,
# then we will not set the global wait for it,
# because if any bug is there due to which an element is not loading then it will wait till the wait time.
# to manage that we will keep global implicit wait for our application as 2 seconds,
# and set the explicit wait for the specific element which will take more time to load.
# we need to create one object of the class 'selenium.webdriver.support.wait' called as 'WebDriverWait'
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
verify_text = driver.find_element(By.CLASS_NAME, "promoInfo").text

assert verify_text == "Code applied ..!"
print(verify_text)