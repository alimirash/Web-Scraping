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

# Configure Chrome options to use your existing Chrome
chrome_options = webdriver.ChromeOptions()

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

# Function to get data for a specific day
def get_data_for_day(date):
    driver.get(f"{url}?day={date}")
    driver.maximize_window()

    # Wait for the page to load completely
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="cal-res-table"]/div[1]/table'))
    # )
    if EC.presence_of_element_located((By.CLASS_NAME, 'Fw(b) Fz(m) Mb(5px) C($tertiaryColor)')):
        return []
    try:
        WebDriverWait(driver, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cal-res-table"]/div[1]/table'))
        )
        # driver.add_cookie()      
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            
        # Get the page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find the table with class name "W(100%)" and get all the rows
        table = soup.find('table', {'class': 'W(100%)'})
        if table:
            rows = table.find_all('tr')
            data_list = []

            # Loop through the rows and get the data
            for row in rows:
                cells = row.find_all('td')
                if not cells:
                    continue
                data_list.append({
                    'Company': cells[0].find('a').text,
                    'EPS': cells[1].text,
                    'Time': cells[2].text,
                    'EPS Estimate': cells[3].text,
                    'Reported EPS': cells[4].text,
                    'Surprise': cells[5].text
                })

            return data_list
    except:
        print("We couldn't find any results.")
        return []
# Set the start date and end date for the range
start_date = datetime.strptime('2010-01-04', '%Y-%m-%d')
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
        day_str = current_date.strftime('%Y-%m-%d')
        print(f"Fetching data for {day_str} ...")

        data_list = get_data_for_day(day_str)
        if data_list:
            # Create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data_list)
            
            # Save the DataFrame to a CSV file
            file_path = os.path.join(output_dir, f"{day_str}.csv")
            df.to_csv(file_path, index=False)
            print(f"Data for {day_str} saved to {file_path}")
        
        # Move to the next day
        current_date += timedelta(days=1)
    else:
        print(f"Data for {day_str}  already exist to {file_path}.")
        current_date += timedelta(days=1)
driver.quit()

print("Data collection complete.")
