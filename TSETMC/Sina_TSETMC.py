from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the page to scrape
url = 'https://www.tsetmc.com/instInfo/50061356691808484'

# Open the browser
driver = webdriver.Chrome()
driver.get(url)

# Click on the menu of the page and click on "حقیقی-حقوقی"
menu = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, 'حقیقی-حقوقی')))
menu.click()

# Wait for the page to load
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'table1')))
time.sleep(4)
response = driver.page_source

# Parse the page
soup = BeautifulSoup(response, 'html.parser')

# Find the tbody tag with id "ClientTypeBody"
tbody = soup.find("tbody", {"id": "ClientTypeBody"})

# Find all the tr tags in the tbody
trs = tbody.find_all("tr")

# Process the tr tags and save to CSV file
data = []
for tr in trs:
    row = [td.text.strip() for td in tr.find_all("td")]
    data.append(row)

# Convert data to DataFrame and save to CSV
df = pd.DataFrame(data)

# Save data to CSV file without headers
filename = 'Sina_TSETMC.csv'
df.to_csv(filename, index=False, header=False, encoding='utf-8-sig')

# Close the browser
driver.quit()
