import os
from bs4 import BeautifulSoup

# Define the directory containing the HTML files
directory = r'isaco\HTML Files'

# Output text file
output_file =  r'isaco\isaco.txt'

# Function to read the file with fallback encodings
def read_file(filepath):
    encodings = ['utf-8-sig' , 'utf-8',  'Windows-1252']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"File {filepath} could not be decoded with tried encodings.")

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as f_output:
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.html') or filename.endswith('.htm'):  # Check if file is an HTML file
            filepath = os.path.join(directory, filename)
            try:
                # Read the file content with fallback encodings
                file_content = read_file(filepath)
                # Parse the HTML content
                soup = BeautifulSoup(file_content, 'html.parser')
                # Extract text from the HTML file
                text = soup.get_text()
                # Write the extracted text to the output file
                f_output.write(text)
            except ValueError as e:
                print(e)

print(f"All text has been extracted and saved to {output_file}.")
