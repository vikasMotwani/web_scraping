from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from urllib.parse import urljoin
from IPython.display import display

companies_df = pd.read_json('company_careers.json', lines=True)

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

#company_careers = 'https://opal.dev/careers'
def scrape_careers(company_careers):

    #company_careers = 'https://www.wander.com/careers'
    try:
        print(company_careers)
        driver.get(company_careers)

        time.sleep(5)

        company_response = driver.page_source.encode('utf-8').strip()
        career_soup = BeautifulSoup(company_response, 'html.parser')
        
        a_tags = career_soup.find_all('a', href=True)
        links = [urljoin(company_careers, a_tag['href']) for a_tag in a_tags if any(keyword in a_tag['href'] for keyword in ['career', 'careers', 'job', 'jobs'])]
        return links
    
    except WebDriverException as e:
        print(f'Error accessing {company_careers}: {e}')
        return []

companies_df['jobs'] = companies_df['careers'].map(scrape_careers)
companies_df.to_json('company_jobs.json', orient='records', lines=True)
#display(companies_df)
