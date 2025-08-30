<h1 align=center>OLX Web Scraper</h1>
<br>

<div align=center>
    <span>🍿</span>
<a href="https://www.youtube.com/watch?v=1tqYgZAPzo0" alt="Video Demo">Video Demo</a>
    <span>🍿</span>
</div>


# 📊 Project Overview

This Python script fetches item listings from OLX (Dubizzle), extracts item names and prices, then calculates the lowest and average prices. It saves the results locally in a CSV for easy access and even handles both English and Arabic languages using regex magic! - Developed as the final project for Harvard's CS50 Python course.

# 🚀 Features

- 🔍 **Fetch Item Listings**: Extracts item details from a given URL.
- 💵 **Price Extraction**: Handles prices formatted in both Arabic and English, including different currency symbols.
- 🧮 **Price Calculation**: Computes the lowest and average prices from the extracted data.
- 📁 **CSV Export**: Saves the item details and prices into a CSV file for further analysis.
- 🌐 **Language Compatibility**: Supports both Arabic and English site languages.

# 🌍 Compatibility
This script is designed to work with webpages in both English and Arabic. It uses regex to handle different currency formats and symbols, making it versatile for various international sites. 

## ⚙️ Prerequisites

To run this script, you need the following Python libraries:

- `requests` : Make HTTP requests to fetch webpage content.
- `beautifulsoup4` : Parse and extract data from HTML.
- `csv` : Write data into a CSV file.

You can install these libraries using pip:

```
pip install requests beautifulsoup4
```
## ▶️ Usage
- **Input Item Link**: Enter the URL of the webpage containing the item listings.
- **Specify Save Folder**: Provide the path where the CSV file should be saved.
    If not specified, the file will be saved in the user's Documents folder by default.

### 🧪 Example
```
Item link: https://example.com/items
Save folder path: C:\Users\YourUsername\Documents\items.csv
```

### 📤 Output
```
Item: 1,234.56 EGP
Item: 4,670.21 EGP

(Showing 10 results)

Lowest Price: 123.45 EGP
Average Price: 678.90 EGP

Do you want to create csv file? (y/n): y
File created successfully!
```

<hr>

### 📜 License
This repository is licensed under the MIT License. See [LICENSE](LICENSE.txt) for more information.
