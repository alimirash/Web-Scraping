from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import requests
import random

# Load stock data
stock_data = pd.read_csv(r'MacroTrend\\TOP_100_Stock_Name.csv', encoding='latin-1', header=None)
base_url = "https://www.macrotrends.net/stocks/charts/"
parameters = ["current-ratio", "roe", "price-book", "debt-equity-ratio", "operating-margin", 
              "basic-shares-outstanding", "cash-flow-from-operating-activities", "receivables-total", 
              "inventory", "net-property-plant-equipment", "free-cash-flow-per-share", "accounts-payable", 
              "book-value-per-share"]

urls = []
for idx in range(1, len(stock_data)):
    for par in parameters:
        urls.append(f"{base_url}{stock_data[1][idx]}/{stock_data[0][idx]}/{par}")

# Setup a requests session
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
})

def fetch_and_save(url, retries=5):
    type_of_data = url.split('/')[-1]
    stock_symbol = url.split('/')[-2]
    stock_ticker = url.split('/')[-3]
    file_path = f'MacroTrend\\htmls\\{stock_ticker}_{type_of_data}.html'
    
    if not os.path.exists(file_path):
        for attempt in range(retries):
            try:
                # Random sleep to avoid detection
                time.sleep(random.randint(5, 15))
                
                response = session.get(url)
                if "Just a moment..." in response.text or response.status_code != 200:
                    print(f"Retrying {url} due to bot detection...")
                    time.sleep(random.randint(20, 40))  # Longer wait before retrying
                    continue
                
                # Save the content if it's valid
                with open(file_path, mode='w') as file:
                    file.write(response.text)
                    print(f'Saved {file_path}')
                break
            except Exception as e:
                print(f"Error fetching {url}: {e}")
                time.sleep(random.randint(20, 40))  # Wait before retrying
    else:
        print(f'{file_path} already exists.')

# Fetch and save all URLs
for url in urls:
    fetch_and_save(url)
