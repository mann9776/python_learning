from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
#  this class can be called to do various other task or setting related to browser like if we want to use headless browser
# which further means browser would be running in background and execute all the processing for which code is written
# this works well with chrome browser

chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("D:/Learning_docs/PythonSelenium/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script(
    "window.scrollBy(0, document.body.scrollHeight);")  # this takes javascript as input and execute it in the broser
driver.get_screenshot_as_file(
    "screen.png")  # takes screenshot after scrolldown or where the browser's page at this moment.
