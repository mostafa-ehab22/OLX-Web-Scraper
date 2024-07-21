# OLX Web Scraper 

## Overview
This Python script is a web scraper designed to fetch item listings from a specified webpage, extract item names and prices, and calculate statistics such as the lowest and average prices. The results are saved in a CSV file for easy review. The script is compatible with webpages that use both English and Arabic languages, thanks to its use of regular expressions (regex) for parsing prices.

## Features
Fetch Item Listings: Extracts item details from a given URL.
Price Extraction: Handles prices formatted in both Arabic and English, including different currency symbols.
Price Calculation: Computes the lowest and average prices from the extracted data.
CSV Export: Saves the item details and prices into a CSV file for further analysis.
Language Compatibility: Supports both Arabic and English site languages.

## Prerequisites
### To run this script, you need the following Python libraries:

**requests:** To make HTTP requests to fetch webpage content.
**beautifulsoup4:** To parse and extract data from HTML.
**csv:** To write data into a CSV file.
__You can install these libraries using pip:__

bash
Copy code
pip install requests beautifulsoup4
Usage
Input Item Link: Enter the URL of the webpage containing the item listings.
Specify Save Folder: Provide the path where the CSV file should be saved. If not specified, the file will be saved in the user's Documents folder by default.

## Example
bash
Copy code
Item link: https://example.com/items
Save folder path: C:\Users\YourUsername\Documents\items.csv

## Functionality
1. get_info()
Prompts the user to input the item link and save folder path. If no save folder path is provided, a default path in the user's Documents folder is used.

2. fetch_listings(link)
Fetches the webpage content from the given URL and parses it to find item listings using BeautifulSoup.

3. add_item_price(item_price, prices)
Extracts the numeric part of the item price from the string, handles both Arabic and English formats, and adds it to the prices list.

4. evaluate_prices(prices)
Calculates the lowest and average prices from the list. Handles cases where the list might be empty or contain invalid data.

5. create_csv(items_details, save_folder)
After prompting user for confirmation, writes the extracted item details and prices into a CSV file at the specified location.

6. main()
Coordinates the execution of the script by calling the above functions and handling user input. Displays the lowest and average prices and optionally saves the data to a CSV file.

## Example Output

Item Name: Example Item
Price: 1,234.56 EGP

(Showing 10 results)

Lowest Price: 123.45 EGP
Average Price: 678.90 EGP