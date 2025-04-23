#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import yaml

service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

# Get free proxies for rotating
def get_free_proxies(driver):
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)

    return proxies


free_proxies = get_free_proxies(driver)

with open('proxy.yml', 'w') as outfile:
    yaml.dump(free_proxies, outfile, default_flow_style=False)
