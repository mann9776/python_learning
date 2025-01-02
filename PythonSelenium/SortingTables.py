import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

service_obj = Service("D:/Learning_docs/PythonSelenium/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
BrowserSortedList = []
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header to sort from browser
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names --> BrowserSortedList [A, B, C]

veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieWebElement:
    BrowserSortedList.append(ele.text)

OriginalSortedList = BrowserSortedList.copy()



# Sort the vegetable list
BrowserSortedList.sort()

assert BrowserSortedList == OriginalSortedList
