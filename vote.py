#!/usr/bin/env python
# import necessary tools from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

# For further enhancements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a fake User Agent
ua = UserAgent()
user_agent = ua.random
print(user_agent)

# set up chrome driver
service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=options)

# Workaround for item not clickable
# https://www.testim.io/blog/selenium-element-is-not-clickable-at-point/
driver.maximize_window()

# navigate to the target webpage
driver.get("https://lms.handwerkswettbewerb.de/ibt/myso/cty/area=site/de/bin/public/voting/details.ibtsico?path=ibt:/division/myso/op/master/voting/2024/1246419951")

#print(driver.page_source)

# Navigate to second page and vote
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Stimme abgeben']"))).click()
driver.implicitly_wait(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Stimme abgeben']"))).click()
driver.implicitly_wait(2)

# Try to get success message
resultMessage = driver.find_element(By.CLASS_NAME, "u-value")

# print the result HTML after JavaScript execution
print(resultMessage.get_attribute('innerHTML'))

# close the browser
driver.quit()
