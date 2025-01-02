from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# There is middleman works when we write code to work in chrome webbrowser which is chrome driver.
# This chrome driver scan all the script or code and send to the chrome browser to execute that is the behind architect.


#service_obj = Service() # We need to start the chrome driver and stopping it
#driver = webdriver.Chrome(service=service_obj)  # start the chrome taking object of the class of service
# Also created a object for the chrome browser to perform all the operations.

#driver.get("https://rahulshettyacademy.com/")

# Also, we can downlad the selenium chrome driver locally and use it by keeping the path in service class.
# So, this is another method to use chrome driver and that makes it our code to execute faster

#service_obj = Service("D:\Learning_docs\PythonSelenium\chromedriver-win64\chromedriver.exe")
service_obj = Service("D:\Learning_docs\PythonSelenium\geckodriver.exe")

#driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Firefox(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/") #  to open the browser
# for property, no brackets are required
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()  #  to close the lbrowser