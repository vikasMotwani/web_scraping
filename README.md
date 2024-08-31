# Startup Company Info Scraper

This project is a web scraper built with Python and BeautifulSoup to collect information about startup companies from a specific website. The goal is to later use this information to find the career pages of these companies and scrape job listings that are suitable.

## Features

- Retrieve startup company names from a specified website
- Parse and extract relevant information using BeautifulSoup
- Find and scrape career pages for job listings
- Extend to filter relevant job posts

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/vikasMotwani/web_scraping.git
    cd web_scraping
    ```

2. **Create a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes:
    ```sh
    requests
    beautifulsoup4
    ```

## Usage

1. **Go to node_backend and Run the npm script:**
    ```sh
    npm run start_all
    ```

    This automatically runs the scraper and opens up a webpage on localhost

2. **Output:**
    - The script will print the names of the startup companies and their career pages to the console and save them to a json
    - The data can be viewed in the started node app using this json
  
## Future Work

- Extract job listings from the career pages and filter them based on suitability.
- Save the collected job data to a structured format (e.g., CSV, database).
