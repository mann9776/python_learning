import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(3)
# implicitly wait max time out is given 5 secs, if page loaded in 2 secs, it will go through and won't wait for whole
# 5secs, so there it can save time also.

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

Expected_values = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
Actual_values = []

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) # time taken in lists does not include in implicitly wait time
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

# chaining of web-element from parent to child , to construct dynamically,
# chaining parent web-element to child web-element using half of the XPATH which is used
# in driver.find_elements and continue with another variable as below:

for result in results:
    Actual_values.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert Expected_values == Actual_values

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# SUM validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

sum1 = 0

for price in prices:
    sum1 = sum1 + int(price.text) # converts text into integer

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum1 == totalAmount



driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# explicit wait used for single element where more time is required in executing the specific element, it will overwrite
# implicit wait time for that element. It can be used with different conditions

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert sum1 > discountAmount





