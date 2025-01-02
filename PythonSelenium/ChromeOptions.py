from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

service_obj = Service("D:/Learning_docs/PythonSelenium/chromedriver-win64/chromedriver.exe")

chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("--start-maximized")

chrom_options.add_argument("headless")
chrom_options.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome(service=service_obj, options=chrom_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)


