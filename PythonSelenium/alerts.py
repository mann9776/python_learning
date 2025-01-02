from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")

driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Manmohan"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert

alertText = alert.text
print(alertText)

assert name in alertText

#alert.accept()
alert.dismiss()