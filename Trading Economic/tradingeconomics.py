import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Read URLs from CSV
stock_data = pd.read_csv('Trading Economic/Trading_Economic_URLs.csv', header=None)
urls = ['https://tradingeconomics.com/united-states/' + str(row[0]) for row in stock_data.values]

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ensure the output directory exists
output_dir = 'Trading Economic/Economics'
os.makedirs(output_dir, exist_ok=True)

# Function to scrape data from a single URL and save to a CSV file
def scrape_data(url, filename):
    driver.get(url)
    time.sleep(7) 

    # Initialize ActionChains
    actions = ActionChains(driver)

    # Prepare a list to store results
    results = []

    # Hover over the chart points and extract data
    points = driver.find_elements(By.CLASS_NAME, "highcharts-point")
    # print(f"Found {len(points)} points at {url}.") 

    for point in points:
        try:
            actions.move_to_element(point).perform()

            # Extract data from tooltip
            date_element = driver.find_element(By.CLASS_NAME, "tooltip-date")
            value_element = driver.find_element(By.CLASS_NAME, "hawk-tt.tooltip-value")

            date = date_element.text
            value = value_element.text

            # Append the result
            results.append({'Date': date, 'Value': value})

        except Exception as e:
            print(f"Error occurred while processing {url}: {e}")

    # Save results to CSV file
    results_df = pd.DataFrame(results)
    results_df.to_csv(filename, index=False)

# Scrape data from all URLs
for idx, url in enumerate(urls):
    # Create a filename for each URL
    filename = os.path.join(output_dir, f'{stock_data.values[idx][0]}.csv')
    scrape_data(url, filename)

# Close the browser
driver.quit()
