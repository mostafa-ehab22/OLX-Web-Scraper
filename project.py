import sys
import os
import re
import csv
import requests
from bs4 import BeautifulSoup

"""
🧨 Mostafa Ehab Yehia 🧨
OLX Web Scraper Project
"""

# ANSI color codes for enhanced printing
class Colors:
    HEADER = '\033[95m'  # Yellow
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'  # Red
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Enhanced printing functions
def print_header(text, is_main=False):
    """Print a styled header"""
    border = "═" * (len(text) + 4)
    color = Colors.RED if is_main else Colors.HEADER
    print(f"\n{color}{Colors.BOLD}{border}")
    print(f"║ {text} ║")
    print(f"{border}{Colors.ENDC}\n")

def print_success(text):
    """Print success message"""
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")

def print_item(index, name, price):
    """Print individual item with formatting"""
    print(f"{Colors.BOLD}{index:3d}.{Colors.ENDC} {Colors.OKCYAN}{name}{Colors.ENDC}")
    print(f"     {Colors.OKGREEN}├─ Price: {price}{Colors.ENDC}")

def print_summary(num_listings, lowest_price, average_price):
    """Print summary statistics with enhanced formatting"""
    print(f"\n{Colors.BOLD}{'─' * 60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}SUMMARY STATISTICS{Colors.ENDC}")
    print(f"{Colors.BOLD}{'─' * 60}{Colors.ENDC}\n")
    
    print(f"{Colors.OKCYAN}Total Listings Found:{Colors.ENDC} {Colors.BOLD}{num_listings}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}Lowest Price:{Colors.ENDC} {Colors.BOLD}{lowest_price:,.2f} EGP{Colors.ENDC}")
    print(f"{Colors.WARNING}Average Price:{Colors.ENDC} {Colors.BOLD}{average_price:,.2f} EGP{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}{'─' * 60}{Colors.ENDC}\n")

def print_progress(current, total):
    """Print progress bar"""
    bar_length = 40
    progress = current / total
    filled = int(bar_length * progress)
    bar = "█" * filled + "░" * (bar_length - filled)
    percentage = progress * 100
    print(f"\r{Colors.OKCYAN}Scraping: [{bar}] {percentage:.1f}% ({current}/{total}){Colors.ENDC}", end='', flush=True)

# User inputs link & Saving folder for CSV
def get_info():
    print_header("OLX WEB SCRAPER - CONFIGURATION")
    
    default_path = os.path.join(os.path.expanduser("~"), "Documents", "output.csv")
    link = input(f"{Colors.OKCYAN}Item link:{Colors.ENDC} ")
    save_folder = input(f"{Colors.OKCYAN}Save folder path (Default: Documents/output.csv):{Colors.ENDC} ")
    print()
    
    # Exit if no link is provided
    if link == "":
        print_error("No link provided. Exiting...")
        sys.exit(1)
    
    # Use default path if no save folder is provided
    if save_folder == "":
        save_folder = default_path
        print_info(f"Using default path: {default_path}")
    
    return (link, save_folder)

# Fetching listings from given webpage
def fetch_listings(link):
    print_info("Fetching listings from webpage...")
    try:
        page = requests.get(link)
        page.raise_for_status()
        src = page.content
        soup = BeautifulSoup(src, "html.parser")
        listings = soup.find_all('div', {'class': 'b5af0448'})
        print_success(f"Found {len(listings)} listings!")
        return listings
    except requests.exceptions.RequestException as e:
        print_error(f"Failed to fetch webpage: {e}")
        sys.exit(1)

# ADDING item price to prices list
def add_item_price(item_price, prices):
    if item_price != "Price not found":
        try:
            match = re.search(r'\d+[\.,\d]*', item_price)
            if match:
                clean_price_str = match.group().replace(",", "")
                clean_price = float(clean_price_str)
                prices.append(clean_price)
        except ValueError:
            pass

# Calculate Lowest & Average Prices 
def evaluate_prices(prices):
    if prices:
        try:
            lowest_price = min(prices)
            average_price = sum(prices) / len(prices)
            return (lowest_price, average_price)
        except (TypeError, ZeroDivisionError) as e:
            print_error(f"Error when evaluating prices: {e}")
            return (0, 0)
    return (0, 0)

# Creating CSV File from items details
def create_csv(items_details, save_folder):
    headers = items_details[0].keys()
    
    try:
        with open(save_folder, 'w', encoding='utf-8') as output_file:
            writer = csv.DictWriter(output_file, headers)
            writer.writeheader()
            writer.writerows(items_details)
            print_success(f"File created successfully at: {save_folder}")
    except IOError as e:
        print_error(f"Failed to create file: {e}")

def main():
    print_header("OLX WEB SCRAPER BY MOSTAFA EHAB YEHIA", is_main=True)
    
    link, save_folder = get_info()
    listings = fetch_listings(link)
    number_of_listings = len(listings)
    
    # Initialize lists to store item details and prices
    items_details = []
    prices = []
    
    print_header("SCRAPING RESULTS")
    
    # Iterate over each listing to extract name and price
    for i in range(number_of_listings):
        print_progress(i + 1, number_of_listings)
        
        # Find item name & price tags
        item_name_tag = listings[i].find('h2', {'class': '_941ffa5e'})
        item_price_tag = listings[i].find('span', {'class': '_1f2a2b47'})
        
        # Extract item name
        if item_name_tag:
            item_name = item_name_tag.text
        else:
            item_name = "Name not found"
        
        # Extract item price       
        if item_price_tag:
            item_price = item_price_tag.text
        else:
            item_price = "Price not found"
        
        # Add item price to prices list
        add_item_price(item_price, prices)
        
        # Add item details to items details list
        items_details.append({'name': item_name, 'price': item_price})
    
    # Clear progress bar and show items
    print("\n")
    for idx, item in enumerate(items_details, 1):
        print_item(idx, item['name'], item['price'])
    
    # Calculate Lowest & Average prices
    lowest_price, average_price = evaluate_prices(prices)
    print_summary(number_of_listings, lowest_price, average_price)
    
    # Prompt user to confirm creation of CSV file
    confirmation = input(f"{Colors.BOLD}Do you want to create CSV file? (y/n):{Colors.ENDC} ").lower().strip()
    if confirmation == 'y':
        create_csv(items_details, save_folder)
    else:
        print_info("CSV file creation cancelled.")

if __name__ == "__main__":
    main()
