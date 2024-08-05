from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from urllib.parse import urljoin
import re

company = 'https://www.harvey.ai/'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

driver.get(company)
time.sleep(30)
response=driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(response, 'html.parser')
print(soup.prettify())
career_link = soup.find_all('a', href=True)
