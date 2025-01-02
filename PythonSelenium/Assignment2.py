from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])

actualText = (driver.find_element(By.CSS_SELECTOR, ".im-para.red").text)

print(actualText)

var = actualText.split(" ")

print(var[4])

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(var[4])

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Manmohan")

driver.find_element(By.XPATH, "//input[@value='user']").click()

dropdown = Select(driver.find_element(By.XPATH, "//select"))

dropdown.select_by_visible_text("Student")

driver.find_element(By.CSS_SELECTOR, ".text-white.termsText").click()

driver.find_element(By.ID, "signInBtn").click()

