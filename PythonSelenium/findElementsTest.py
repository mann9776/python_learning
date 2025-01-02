import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")

driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")  # plural find_elements return with list as the CSS selector used here has multiple matching elements
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text)

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
