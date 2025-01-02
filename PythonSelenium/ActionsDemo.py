#import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)

driver.implicitly_wait(5)
driver.maximize_window()
# implicitly wait max time out is given 5 secs, if page loaded in 2 secs, it will go through and won't wait for whole
# 5secs, so there it can save time also.

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)  # to perform mouse actions

#action.double_click(driver.find_element(By.CSS_SELECTOR, ""))
#action.context_click() # right click action
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()