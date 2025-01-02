from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)
driver.get("http://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I can automate in frames")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
