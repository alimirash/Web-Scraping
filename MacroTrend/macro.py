from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import gc

stock_path = os.path.join(r'MacroTrend\\TOP_100_Stock_Name.csv')
stock_data = pd.read_csv(stock_path, encoding='latin-1' , header=None)
base_url = "https://www.macrotrends.net/stocks/charts/"
Parameters = ["current-ratio" , "roe" , "price-book" , "debt-equity-ratio" , "operating-margin" , "basic-shares-outstanding" ,
            "cash-flow-from-operating-activities" , "receivables-total" , "inventory" , "net-property-plant-equipment" ,
            "free-cash-flow-per-share" , "accounts-payable" , "book-value-per-share"]

urls = []
for idx in range(1, len(stock_data)):
    for par in Parameters:
        urls.append('https://www.macrotrends.net/stocks/charts/' + str(stock_data[1][idx]) + '/' + str(stock_data[0][idx]) + '/' + str(par))
def parse_page(driver):
    left_table = []
    right_table = []

    driver.execute_script("window.scrollTo(0 , 1500)")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # get the thead tag in table with Xpath : //*[@id="style-1"]/div[1]/table
    thead = soup.find_all('thead')
    tbody = soup.find_all('tbody')
    left_thead = thead[0] 
    # get tr in thead tag and th in tr tag and save text in list
    left_thead_th = left_thead.find_all('th') 
    left_thead_th_text = [th.text for th in left_thead_th]
    left_table.append(left_thead_th_text)

    left_tbody = tbody[0]
    left_tbody_tr = left_tbody.find_all('tr')
    for tr in left_tbody_tr:
        left_tbody_td = tr.find_all('td')
        left_tbody_td_text = [td.text for td in left_tbody_td]
        left_table.append(left_tbody_td_text)
    
    # get the thead tag in table with Xpath : //*[@id="style-1"]/div[2]/table
    right_thead = thead[1]
    # get tr in thead tag and th in tr tag and save text in list
    right_thead_th = right_thead.find_all('th')
    right_thead_th_text = [th.text for th in right_thead_th]
    right_table.append(right_thead_th_text)
    
    right_tbody = tbody[1]
    right_tbody_tr = right_tbody.find_all('tr')
    for tr in right_tbody_tr:
        right_tbody_td = tr.find_all('td')
        right_tbody_td_text = [td.text for td in right_tbody_td]
        right_table.append(right_tbody_td_text)

    return left_table , right_table


for count, url in enumerate(urls):
    type_of_data = url.split('/')[-1]
    filename = f'{type_of_data}\\{stock_data[1][count + 1]}_{type_of_data}_Annual_Revenue.csv'
    # Check if the file exists
    if not os.path.exists(filename):
        try: 
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--allow-running-insecure-content')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            driver.implicitly_wait(5)
            driver.maximize_window()
            # Wait for the page to load
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "main_content"))
            )
            
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "Button__StyledButton-a1qza5-0 jkvvVr"))).click()
            except:
                print("No cookie consent pop-up found or failed to click 'Accept all'.")
        
            # Get the page source
            left_table , right_table = parse_page(driver)
            # Create a DataFrame
            left_df = pd.DataFrame(left_table)
            right_df = pd.DataFrame(right_table)
            # Check if the folder exists, if not, create it
            if not os.path.exists(type_of_data):
                os.makedirs(type_of_data)

            # Construct the full file paths for the CSV files
            annual_path = os.path.join(f'{type_of_data}\\{stock_data[1][count + 1]}_{type_of_data}_Annual_Revenue.csv')
            quarterly_path = os.path.join(f'{type_of_data}\\{stock_data[1][count + 1]}_{type_of_data}_Quarterly_Revenue.csv')

            # Save the DataFrames to the CSV files
            left_df.to_csv(annual_path, index=False, header=None)
            right_df.to_csv(quarterly_path, index=False, header=None)
            print("Save " + str(stock_data[1][count + 1]) + f" On {type_of_data}")
            # Close the browser
            driver.quit()
        except:
            print("Error On " + str(stock_data[1][count + 1]))
            driver.quit()
    else:
        print(stock_data[0][count + 1] + f"_{type_of_data}" + " already exist.")
