#!/usr/bin/env python
# import necessary tools from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pprint

# # Create virtual display
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

# For further enhancements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up chrome driver
service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".u-button"))
)


# navigate to the target webpage
driver.get("https://lms.handwerkswettbewerb.de/ibt/myso/cty/area=site/de/bin/public/voting/details.ibtsico?path=ibt:/division/myso/op/master/voting/2024/1246419951")

#print(driver.page_source)

# Navigate to second page and vote
voteButton = driver.find_element("xpath", '//button[@title="Stimme abgeben"]')
print(dir(voteButton))
print("JL->",voteButton.get_attribute('innerHTML'))
print(voteButton.get_attribute)
voteButton.click()
voteButton2 = driver.find_element("xpath", '//button[@title="Stimme abgeben"]')
voteButton2.click()

# Try to get success message
resultMessage = driver.find_element(By.CLASS_NAME, "u-value")

# print the result HTML after JavaScript execution
print(resultMessage.get_attribute('innerHTML'))

# close the browser
driver.quit()

