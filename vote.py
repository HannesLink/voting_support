#!/usr/bin/env python
# import necessary tools from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up chrome driver
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

# navigate to the target webpage
driver.get("https://lms.handwerkswettbewerb.de/ibt/myso/cty/area=site/de/bin/public/voting/details.ibtsico?path=ibt:/division/myso/op/master/voting/2024/1246419951")

# wait for the product grid to load
#WebDriverWait(driver, 10).until(
#    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#product-grid .product-item"))
#)

voteButton = driver.find_element("xpath", '//*[@title="Stimme abgeben"]')
voteButton.click();
voteButton2 = driver.find_element("xpath", '//*[@title="Stimme abgeben"]')
voteButton2.click();

resultMessage = driver.find_element(By.CLASS_NAME, "u-value")


# print the result HTML after JavaScript execution
print(resultMessage.get_attribute('innerHTML'))


# close the browser
driver.quit()

