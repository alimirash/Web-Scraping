from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# URL for Yahoo Finance earnings calendar
url = "https://finance.yahoo.com/calendar/earnings"

# Parameters for the request
params = {'from': '2024-06-16', 'to': '2024-06-22', 'day': '2024-06-20'}

# Configure Chrome options to use your existing Chrome
chrome_options = webdriver.ChromeOptions()

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

# Navigate to the URL
driver.get(f"{url}?from={params['from']}&to={params['to']}&day={params['day']}")
driver.maximize_window()

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.secondary.accept-all"))).click()
except Exception as e:
    print(f"No cookie consent pop-up found or failed to click 'Accept all'. Error: {e}")


# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.W(100%)'))
)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# Get the page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')


# Find the Table with Class Name "W(100%)" and get all the rows and save them in a list
table = soup.find('table', {'class': 'W(100%)'})
rows = table.find_all('tr')

# Loop through the rows and get the data
for row in rows:
    data = row.find_all('td')
    if len(data) == 0:
        continue
    company = data[0].find('a').text
    eps = data[1].text
    time = data[2].text
    EPS_Estimate = data[3].text
    Reported_EPS = data[4].text
    Surprise = data[5].text
    print(company, eps, time, EPS_Estimate, Reported_EPS, Surprise)


driver.quit()