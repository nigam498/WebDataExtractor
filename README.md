WebDataExtractor
WebDataExtractor is a Python-based tool that allows users to extract data from websites and save it into CSV files. The tool provides a simple GUI for user interaction using the tkinter library.

Features
Download HTML content from a specified URL.
Extract data such as hyperlinks and paragraphs from the HTML.
Save extracted data into separate CSV files.
Simple and user-friendly GUI.
Requirements
Python 3.x
requests library
beautifulsoup4 library
pandas library
tkinter library (usually included with Python)
Installation
Clone the Repository

bash
git clone https://github.com/yourusername/WebDataExtractor.git
cd WebDataExtractor
Install Required Libraries

You can install the required libraries using pip:

bash
pip install -r requirements.txt
Or install them individually:

bash
pip install requests beautifulsoup4 pandas
Usage
Run the Application

bash
python web_data_extractor.py
Using the GUI

Enter the URL of the website you want to extract data from.
Click on the "Download and Extract Data" button.
Choose the directory where you want to save the CSV files.
The tool will extract hyperlinks and paragraphs from the specified URL and save them into links.csv and paragraphs.csv respectively in the chosen directory.
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or suggestions, feel free to open an issue or contact us at [nigampatel498@gmail.com].
Code
Here is the main script (web_data_extractor.py):

python
Copy code
import tkinter as tk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to download and parse website data
def download_website_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from HTML (example: extracting links and paragraphs)
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    paragraphs = [p.get_text() for p in soup.find_all('p')]

    # Extract data from CSS and JavaScript can be more complex and specific to the use case

    # Example DataFrames
    df_links = pd.DataFrame(links, columns=['Links'])
    df_paragraphs = pd.DataFrame(paragraphs, columns=['Paragraphs'])

    return df_links, df_paragraphs

# Function to save data to CSV
def save_to_csv(dataframes, filenames):
    for df, filename in zip(dataframes, filenames):
        df.to_csv(filename, index=False)

# Function to handle button click
def on_button_click():
    url = url_entry.get()
    df_links, df_paragraphs = download_website_data(url)

    # Ask user where to save the files
    file_path = filedialog.askdirectory()

    # Save DataFrames to CSV files
    save_to_csv([df_links, df_paragraphs], [f"{file_path}/links.csv", f"{file_path}/paragraphs.csv"])

    tk.messagebox.showinfo("Success", "Data extracted and saved to CSV files successfully.")

# Create the GUI
root = tk.Tk()
root.title("WebDataExtractor")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download and Extract Data", command=on_button_click)
download_button.pack(pady=20)

root.mainloop()
Requirements File
Create a requirements.txt file with the following contents:

Requirements File

requests
beautifulsoup4
pandas
Feel free to customize the guide and code as per your specific needs before publishing it to GitHub.






