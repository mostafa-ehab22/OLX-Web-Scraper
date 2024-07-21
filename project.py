import sys
import os
import re
import csv
import requests
from bs4 import BeautifulSoup

# User inputs link & Saving folder for csv
def get_info():
    default_path = os.path.join(os.path.expanduser("~"), "Documents", "output.csv")
    link = input("\nItem link: ")
    save_folder = input("\nSave folder path (Default: Documents\ouput.csv): ")
    
    if link == "":
        sys.exit("No link provided. Exiting...")

    if save_folder == "":
        save_folder = default_path
    
    return (link, save_folder)

# Fetching listings from webpage
def fetch_listings(link):
    page = requests.get(link)
    src = page.content # Page content (Byte code)
    soup = BeautifulSoup(src, "html.parser") # Parsing page

    # Fetching items listings on webpage
    listings = soup.find_all('div', {'class': 'b5af0448'})
    return listings

# ADDING item price to prices list
def add_item_price(item_price, prices):
    if item_price != "Price not found":
        try:
            # Use regex to extract numeric part of the price
            match = re.search(r'\d+[\.,\d]*', item_price)
            if match:
                # Replace commas & periods if necessary,  
                # Convert to float
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
        except (TypeError, ZeroDivisionError):
            print(f"Error when evaluating prices: {e}")

# Creating csv File
def create_csv(items_details, save_folder):
    headers = items_details[0].keys()
    
    with open(save_folder, 'w', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, headers)
        writer.writeheader()
        writer.writerows(items_details)
        print("File successfully created")



def main():
    link, save_folder = get_info()
    listings = fetch_listings(link)
    number_of_listings = len(listings)

    # Initialize items details list
    items_details = []
    # Initialize prices list
    prices = []
    
    # Getting name & price of each item
    for i in range(number_of_listings):

        # Find item name & price
        item_name_tag = listings[i].find('h2', {'class': '_941ffa5e'})
        item_price_tag = listings[i].find('span', {'class': '_1f2a2b47'})

        # Check if item name exists
        if item_name_tag:
            item_name = item_name_tag.text
        else:
            item_name = "Name not found"
        
        # Check if item price exists        
        if item_price_tag:
            item_price = item_price_tag.text
        else:
            item_price = "Price not found"
        
        # Adding item price => prices list
        add_item_price(item_price,prices)
        
        # Adding item info => Items details list
        items_details.append({'name': item_name, 'price': item_price})
        
        print(f"{item_name} : {item_price}")

    # Get Lowest & Average Price
    lowest_price, average_price = evaluate_prices(prices)

    print(f"\n(Showing {number_of_listings} results)\n")
    print(f"Lowest Price: {lowest_price:,.2f} EGP")
    print(f"Average Price: {average_price:,.2f} EGP\n")


    # Creating CSV File
    confirmation = input("Do you want to create csv file? (y/n): ").lower().strip()
    if confirmation == 'y':
        create_csv(items_details, save_folder)



if __name__ == "__main__":
    main()