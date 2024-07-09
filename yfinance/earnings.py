import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time

# URL for Yahoo Finance earnings calendar
url = "https://finance.yahoo.com/calendar/earnings"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

# Function to get data for a specific day
def get_data_for_day(date):
    driver.get(f"{url}?day={date}")
    driver.maximize_window()
    
    data_list = []

    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cal-res-table"]/div[1]/table'))
            )
            
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                
            # Get the page source and parse with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Find the table with class name "W(100%)" and get all the rows
            table = soup.find('table', {'class': 'W(100%)'})
            if table:
                rows = table.find_all('tr')

                # Loop through the rows and get the data
                for row in rows:
                    cells = row.find_all('td')
                    if not cells:
                        continue
                    data_list.append({
                        'Symbol': cells[0].find('a').text if cells[0].find('a') else '',
                        'Company': cells[1].text,
                        'Event Name': cells[2].text,
                        'Earnings Call Time': cells[3].text,
                        'EPS Estimate': cells[4].text,
                        'Reported EPS': cells[5].text,
                        'Surprise(%)': cells[6].text
                    })
            
            # Check for the "Next" button and click it
            next_button = driver.find_element(By.XPATH, '//*[@id="cal-res-table"]/div[2]/button[3]')
            aria_disabled = next_button.get_attribute('aria-disabled')
            if aria_disabled == 'false':
                next_button.click()
                # Wait for the new content to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="cal-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a'))
                )
                time.sleep(2)  # Adding extra wait time to ensure content is fully loaded

                # Check if the content has changed
                new_soup = BeautifulSoup(driver.page_source, 'html.parser')
                new_table = new_soup.find('table', {'class': 'W(100%)'})
                if new_table == table:
                    break  # Exit the loop if the table has not changed
            else:
                break

        except Exception as e:
            print(f"Error fetching data for {date}: {e}")
            break

    return data_list

# Set the start date and end date for the range
start_date = datetime.strptime('2023-01-26', '%Y-%m-%d')
end_date = datetime.now()

# Ensure the directory for saving CSV files exists
output_dir = 'Earnings'
os.makedirs(output_dir, exist_ok=True)

# Loop through each day in the date range
current_date = start_date
while current_date <= end_date:

    day_str = current_date.strftime('%Y-%m-%d')
    file_path = os.path.join(output_dir, f"earnings_{day_str}.csv")
    if not os.path.exists(file_path):
        time.sleep(0.3)
        print(f"Fetching data for {day_str} ...")

        data_list = get_data_for_day(day_str)
        if data_list:
            # Create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data_list)
            
            # Save the DataFrame to a CSV file
            df.to_csv(file_path, index=False)
            print(f"Data for {day_str} saved to {file_path}")
        else:
            print(f"No data for {day_str}")
        
    else:
        print(f"Data for {day_str} already exists at {file_path}.")
        
    # Move to the next day
    current_date += timedelta(days=1)

driver.quit()

print("Data collection complete.")
