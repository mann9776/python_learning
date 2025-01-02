from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# to fill up the form in a url in browser, we can find fields with following params or keyword
# ID, Xpath, CSSSelector, classname, name, linktext
# Use mostly ID
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# For CSS selector
# tagname[attribute='value']

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Manmohan")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


# static dropdown - where we have limited or very options for selecting one from dropdown

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()


# we can construct xpath following up a syntax
# //tagname[@attribute='value'],
# if multiple XPATHs are having same attribute and name then we can use index - suppose 3 xpath matches are there
# use as - //tagname([@attribute='value'])[3] - if 3rd option need to take for filling up in form

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message  # can be used if test case is pass or fail

# other examples for CSS selectors - #id or .className

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
