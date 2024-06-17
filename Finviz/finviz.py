import requests
import csv
from bs4 import BeautifulSoup

# Function to scrape data from a single page with a constant "c" parameter
def scrape_page(base_url, page_number):
    url = f"{base_url}&r={page_number}&c=0,1,2,3,4,5,6,7,8,9,10,13,74,18,127,128,33,35,41,48,51,62,67,65,66"
    
    # Add headers to mimic a legitimate browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <tr> elements with the specified class name
        tr_elements = soup.find_all("tr", class_="styled-row is-hoverable is-bordered is-rounded is-striped has-color-text")

        # Extract data from each <tr> element
        page_data = []
        for tr in tr_elements:
            # Find all <td> elements within the current <tr> element
            td_elements = tr.find_all("td")
            
            # Extract data from each <td> element
            row_data = [td.text.strip() for td in td_elements]
            page_data.append(row_data)

        # Don't forget to close the connection
        response.close()

        return page_data
    else:
        print("Failed to retrieve page. Status code:", response.status_code)
        return None

# Main function to scrape data from all pages
def scrape_all_pages(base_url, total_pages):
    all_data = []
    for page_number in range(1, total_pages + 1):
        page_data = scrape_page(base_url, page_number * 20 - 19)
        if page_data:
            all_data.extend(page_data)

    return all_data

# URL base
base_url = "https://finviz.com/screener.ashx?v=152"

# Total number of pages
total_pages = 476

# Scrape data from all pages
all_data = scrape_all_pages(base_url, total_pages)

# Save data to CSV file
with open("scraped_data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)

print("Data has been successfully saved to 'scraped_data.csv'.")
