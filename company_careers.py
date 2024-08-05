#install and import librariess
#in terminal run: pip install -r requirements.txt

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from urllib.parse import urljoin
import re 

#setup connection to apis
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

def get_companies_url(url):
  links = []
  driver.get(url)
  time.sleep(5)
  response=driver.page_source.encode('utf-8').strip()
  soup = BeautifulSoup(response, 'html.parser')
  result = soup.find('div', {'class': 'infinite-container'})
  li =  result.find_all('div', {'class': 'infinite-item'})
  for i in li:
    c = i.find('a', {'id': 'startup-website-link'}, text=True, href=True)
    if not c:
      continue
    company = { 'name': c.text , 'link': c['href'].replace('?utm_source=topstartups.io', '') }
    links.append(company)
  return soup, links

def next_page(soup):
  pagination = soup.find('a', {'class': 'infinite-more-link'})
  if pagination and 'href' in pagination.attrs:
    return pagination['href']

def get_careers_href(company):
  try:
    driver.get(company)
    print(company)
    time.sleep(5)
    response=driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(response, 'html.parser')

    patterns = [
    re.compile(r'\W*\bcareers?\b\W*', re.IGNORECASE),            # matches 'career' or 'careers'
    re.compile(r'\W*\bjobs?\b\W*', re.IGNORECASE),               # matches 'job' or 'jobs'
    re.compile(r'\W*\bjoin\s+us\b\W*', re.IGNORECASE),           # matches 'join us'
    ]
    
    for pattern in patterns:
      career_link = soup.find('a', href=True, text=pattern)
      if career_link:
        career_href = urljoin(company, career_link['href'])
        print(career_href)
        if check_link(career_href):
          return career_href
    return None
    
  except WebDriverException as e:
    return None
  
def check_link(url):
    try:
        driver.get(url)
        return url
    except Exception as e:
        return False
    
def main(base_url, max_pages):
  companies = []
  soup, page_links = get_companies_url(base_url)
  companies.extend(page_links)
  for i in range(1, max_pages):
    url = next_page(soup)
    if not url:
      print(f'Only {i} pages exist')
      break
    target_url = f'https://topstartups.io/{url}'
    soup, page_links = get_companies_url(target_url)
    companies.extend(page_links)
  companies_df = pd.DataFrame(companies)
  companies_df['careers'] = companies_df['link'].map(get_careers_href)
  companies_final = companies_df.dropna()
  print(companies_df)
  print(companies_final)
  companies_final.to_json('company_careers.json', orient='records', lines=True)

if __name__ == '__main__':
  base_url = 'https://topstartups.io/?hq_location=USA'
  max_pages = 1
  main(base_url, max_pages)
  ## Todo: use regex to match anything with careers. Use bs4 to find descendents with Career text
  