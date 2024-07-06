from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
<<<<<<< HEAD
import os

stock_data = pd.read_csv('MacroTrend\MacroTrend_Stocks.csv', encoding='latin-1' , header=None)

financial_ratios_URLs = []
for i in range(1, len(stock_data)):
    financial_ratios_URLs.append('https://www.macrotrends.net/stocks/charts/' + str(stock_data[1][i]) + '/' + str(stock_data[0][i]) + '/financial-ratios')

=======
>>>>>>> e2d45ed1a0f62ba7ae84eebe0386f1f9acce9666

def parse_page(driver):
    # Scroll to the bottom of the page to load all the data
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Scroll horizontally to load all the data
<<<<<<< HEAD
    # try:
    #     for _ in range(50):
    #         WebDriverWait(driver , 5).until(EC.element_to_be_clickable(By.XPATH , '//*[@id="jqxScrollBtnDownhorizontalScrollBarjqxgrid"]')).click()
    # # scroll_element = driver.find_element(By.XPATH, "//div[@id='jqxScrollBtnDownhorizontalScrollBarjqxgrid']/div")
    # # driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_element)
    #     # time.sleep(2)  # Wait for the data to load after scrolling
    # except Exception as e:
    #     print(f"No horizontal scroll bar found or failed to scroll: {e}")


=======
    try:
        scroll_element = driver.find_element(By.ID, "horizontalScrollBarjqxgrid")
        driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_element)
        time.sleep(2)  # Wait for the data to load after scrolling
    except Exception as e:
        print(f"No horizontal scroll bar found or failed to scroll: {e}")


    try:
        element = driver.find_element_by_class_name("jqx-reset")
        for _ in range(50):
            element.click()
    except:
        print("No Scroll Button Found")

>>>>>>> e2d45ed1a0f62ba7ae84eebe0386f1f9acce9666
    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    
    header_main_div = soup.find('div', {"id": "columntablejqxgrid"})
    
    first_div = soup.find("div", {"id": "contenttablejqxgrid"})
    divs = first_div.find_all("div", {"id": lambda x: x and x.startswith("row")})
    
    page_data = []

    # Extract header data
    header_data = []
    header_divs = header_main_div.find_all("div", {"class": "jqx-grid-column-header jqx-widget-header"})
    for div in header_divs:
        cell = div.find("span", {"style": lambda x : x.startswith("text-overflow")})
        header_data.append(cell.text.strip())
    page_data.append(header_data)

    # Extract row data
    for div in divs:
        table_row = div.find_all("div", {"class": lambda x: x and x.startswith("jqx-grid-cell jqx-item")})
        row_data = [cell.text.strip() for cell in table_row]
        page_data.append(row_data)
        
    return page_data


<<<<<<< HEAD
for count, url in enumerate(financial_ratios_URLs):
    filename = f'Financial Ratios/{stock_data[0][count + 1]}_Financial_Ratios.csv'
    # Check if the file exists
    if not os.path.exists(filename):
        try: 
            time.sleep(2)
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)
            driver.get(url)
            driver.maximize_window()
            # Wait for the page to load
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "main_content"))
            )
            
            data = []
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Button__StyledButton-a1qza5-0.jkvvVr"))).click()
            except:
                print("No cookie consent pop-up found or failed to click 'Accept all'.")
        
            # Get the page source
            data += parse_page(driver)
            df = pd.DataFrame(data)
            df.to_csv(f'Financial Ratios\{stock_data[0][count + 1]}_Financial_Ratios.csv', index=False , header=None)
            print("Save " + str(stock_data[0][count + 1]) + " On Financial Ratios")
            # Close the browser
            driver.quit()
        except:
            print("Error On " + str(stock_data[0][count + 1]))
    else:
        print(stock_data[0][count + 1] + "_Financial_Ratios" + " already exist.")
=======
url = 'https://www.macrotrends.net/stocks/charts/AAPL/apple/financial-ratios'
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
# Wait for the page to load
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "main_content"))
)

data = []
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Button__StyledButton-a1qza5-0.jkvvVr"))).click()
except:
    print("No cookie consent pop-up found or failed to click 'Accept all'.")

# Get the page source
data += parse_page(driver)
df = pd.DataFrame(data)
df.to_csv('MacroTrend\Financial Ratios\Financial_Ratios.csv', index=False , header=None)
# Close the browser
driver.quit()
>>>>>>> e2d45ed1a0f62ba7ae84eebe0386f1f9acce9666
