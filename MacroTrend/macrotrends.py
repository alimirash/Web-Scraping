from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.macrotrends.net/stocks/stock-screener"

# Open the browser
driver = webdriver.Chrome()
driver.get(URL)

# Click on the "Revenue & Earnings" tab
menu = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, "Revenue & Earnings")))
menu.click()

data = []

# Define a helper function to parse the page content
def parse_page():
    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    first_div = soup.find("div", {"id": "contenttablejqxGrid"})
    divs = first_div.find_all("div", {"id": lambda x: x and x.startswith("row")})
    
    page_data = []
    for div in divs:
        table_row = div.find_all("div", {"class": lambda x: x and x.startswith("jqx-grid-cell jqx-item")})
        row_data = [cell.text.strip() for cell in table_row]
        page_data.append(row_data)
    return page_data

# Loop through the pages
for i in range(280):
    # Parse the current page
    data.extend(parse_page())
    
    # Go to the next page
    try:
        next_page = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='next']")))
        next_page.click()
        
    except:
        print(f"Failed to click on the next button on page {i+1}")
        break

# Convert data to DataFrame
df = pd.DataFrame(data, columns=["Stock Name", "Ticker", "12 Month Sales Growth", "5 Year Sales Growth", "12 Month EPS Growth", "5 Year EPS Growth", "Last Quarter EPS Surprise %", "Estimated EPS Growth Next Year"])

# Save data to CSV file
filename = "macrotrends.csv"
df.to_csv(filename, index=False, encoding="utf-8-sig")

# Close the browser
driver.close()
