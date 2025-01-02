from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo1254@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("hello@123456")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("hello@123456")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


