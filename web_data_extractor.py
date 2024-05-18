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
root.title("Website Data Extractor")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download and Extract Data", command=on_button_click)
download_button.pack(pady=20)

root.mainloop()
