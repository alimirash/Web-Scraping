from bs4 import BeautifulSoup
import pandas as pd
import os

def parse_page_from_file(file_path):
    left_table = []
    right_table = []

    # Read the HTML content from the file (UTF-8 / latin1)
    with open(file_path, 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Get the thead and tbody tags
    thead = soup.find_all('thead')
    tbody = soup.find_all('tbody')

    # Check if there are enough thead and tbody tags
    if len(thead) < 2 or len(tbody) < 2:
        print(f"Warning: The structure of the file {file_path} is not as expected.")
        return None, None

    # Left table
    left_thead = thead[0] 
    left_thead_th = left_thead.find_all('th') 
    left_thead_th_text = [th.text.strip() for th in left_thead_th]
    left_table.append(left_thead_th_text)

    left_tbody = tbody[0]
    left_tbody_tr = left_tbody.find_all('tr')
    for tr in left_tbody_tr:
        left_tbody_td = tr.find_all('td')
        left_tbody_td_text = [td.text.strip() for td in left_tbody_td]
        left_table.append(left_tbody_td_text)
    
    # Right table
    right_thead = thead[1]
    right_thead_th = right_thead.find_all('th')
    right_thead_th_text = [th.text.strip() for th in right_thead_th]
    right_table.append(right_thead_th_text)
    
    right_tbody = tbody[1]
    right_tbody_tr = right_tbody.find_all('tr')
    for tr in right_tbody_tr:
        right_tbody_td = tr.find_all('td')
        right_tbody_td_text = [td.text.strip() for td in right_tbody_td]
        right_table.append(right_tbody_td_text)

    return left_table, right_table

# Directory where your HTML files are stored
html_dir = "MacroTrend\htmls"

for file_name in os.listdir(html_dir):
    if file_name.endswith(".html"):
        stock_ticker, type_of_data = file_name.split('_')[0], file_name.split('_')[1].replace('.html', '')
        
        Annual_file_name = f'MacroTrend\\{type_of_data}\\{stock_ticker}_{type_of_data}_Annual_Revenue.csv'
        Quarterly_file_name = f'MacroTrend\\{type_of_data}\\{stock_ticker}_{type_of_data}_Quarterly_Revenue.csv'

        if not os.path.exists(Quarterly_file_name) or not os.path.exists(Annual_file_name):
            file_path = os.path.join(html_dir, file_name)
            try:
                left_table, right_table = parse_page_from_file(file_path)

                # Skip processing if the file structure was not as expected
                if left_table is None or right_table is None:
                    continue

                # Create DataFrames
                left_df = pd.DataFrame(left_table)
                right_df = pd.DataFrame(right_table)

                # Check if the folder exists, if not, create it
                if not os.path.exists(f'MacroTrend\\{type_of_data}'):
                    os.makedirs(f'MacroTrend\\{type_of_data}')

                # Save the DataFrames to the CSV files
                annual_path = os.path.join(f'MacroTrend\\{type_of_data}\\{stock_ticker}_{type_of_data}_Annual_Revenue.csv')
                quarterly_path = os.path.join(f'MacroTrend\\{type_of_data}\\{stock_ticker}_{type_of_data}_Quarterly_Revenue.csv')

                left_df.to_csv(annual_path, index=False, header=None)
                right_df.to_csv(quarterly_path, index=False, header=None)

                print(f"Saved {stock_ticker} on {type_of_data}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
        else:
            print(f"{stock_ticker}_{type_of_data} already exists.")
