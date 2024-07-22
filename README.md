<h1 align=center>OLX Web Scraper</h1>
<br>

<div align=center>
    <span>🍿</span>
<a href="https://www.youtube.com/watch?v=1tqYgZAPzo0" alt="Video Demo">Video Demo</a>
    <span>🍿</span>
</div>


# Overview

This Python script is a web scraper designed to fetch item listings from OLX, extract item names and prices, and calculate statistics such as the lowest and average prices. The results are saved in a CSV file for easy review. The script is compatible with webpages that use both English and Arabic languages, thanks to its use of regular expressions (regex) for parsing prices.

# Features

- **Fetch Item Listings**: Extracts item details from a given URL.
- **Price Extraction**: Handles prices formatted in both Arabic and English, including different currency symbols.
- **Price Calculation**: Computes the lowest and average prices from the extracted data.
- **CSV Export**: Saves the item details and prices into a CSV file for further analysis.
- **Language Compatibility**: Supports both Arabic and English site languages.

# Compatibility
This script is designed to work with webpages in both Arabic and English. It uses regex to handle different currency formats and symbols, making it versatile for various international sites.

<br>

## Prerequisites

To run this script, you need the following Python libraries:

- `requests` : Make HTTP requests to fetch webpage content.
- `beautifulsoup4` : Parse and extract data from HTML.
- `csv` : Write data into a CSV file.

You can install these libraries using pip:

```
pip install requests beautifulsoup4
```
## Usage
- **Input Item Link**: Enter the URL of the webpage containing the item listings.
- **Specify Save Folder**: Provide the path where the CSV file should be saved.
    If not specified, the file will be saved in the user's Documents folder by default.

### Example
```
Item link: https://example.com/items
Save folder path: C:\Users\YourUsername\Documents\items.csv
```

### Output
```
Item Name: Example Item
Price: 1,234.56 EGP

(Showing 10 results)

Lowest Price: 123.45 EGP
Average Price: 678.90 EGP

Do you want to create csv file? (y/n):
```
