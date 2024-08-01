from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from urllib.parse import urljoin
import requests

company = 'http://quantumcircuits.com/'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

driver.get(company)
time.sleep(10)
response=driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(response, 'html.parser')
print(soup.find_all('a'))
career_link = soup.find('a', href=True, text='Careers')
print(career_link)
if career_link:
    career_href = urljoin(company, career_link['href'])
print(career_href)
try:
        driver.get(career_href)
        print(career_href)
except Exception as e:
        print(f"Error: {e} for URL: {url}")