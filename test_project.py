import os
import pytest
import requests
import csv
from project import get_info, fetch_listings, add_item_price, evaluate_prices, create_csv


def test_get_info(monkeypatch):
    # Test with user providing both link & save folder
    input_values = iter(["http://example.com", "custom_folder/output.csv"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    assert get_info() == ("http://example.com", "custom_folder/output.csv")

    # Test with user providing no link (should trigger SystemExit)
    monkeypatch.setattr('builtins.input', lambda _: "")
    with pytest.raises(SystemExit):
        get_info()



def test_fetch_listings(monkeypatch):
    # Define a mock response class to simulate HTTP response
    class MockResponse:
        @property
        def content(self):
            # Simulate HTML content with a byte string
            return b'<div class="b5af0448">Listing</div>' 
        
    # Using monkeypatch: Replace requests.get with a lambda function => Returns a MockResponse instance
    monkeypatch.setattr(requests, 'get', lambda _: MockResponse())
    
    # Call fetch_listings with a test URL
    listings = fetch_listings("http://example.com")
    
    # Assert that exactly one listing was found
    assert len(listings) == 1
    
    # Assert that the text content of the first listing matches "Listing"
    assert listings[0].text == "Listing"



def test_add_item_price():
    prices = []
    
    # Test adding a valid price string
    add_item_price("1000", prices)
    assert prices == [1000.0]
    
    # Test with a price string indicating no price found
    add_item_price("Price not found", prices)
    assert prices == [1000.0]
    
    # Test with an invalid price string
    add_item_price("Invalid price", prices)
    assert prices == [1000.0]



def test_evaluate_prices():
    # Test with a list of prices
    prices = [100, 200, 300]
    lowest_price, average_price = evaluate_prices(prices)
    assert lowest_price == 100
    assert average_price == 200
    
    # Test with an empty list of prices
    assert evaluate_prices([]) == None



def test_create_csv(tmp_path):
    items_details = [{'name': 'Item1', 'price': 100}, {'name': 'Item2', 'price': 200}]
    
    # Use tmp_path fixture to create a temporary file path
    save_folder = tmp_path / "output.csv"
    
    # Call create_csv to create the CSV file
    create_csv(items_details, save_folder)
    
    # Assert that the file was created
    assert save_folder.exists()
    
    # Read the created CSV file and verify its content
    with open(save_folder, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        # Verify that the CSV contains the correct number of rows
        assert len(rows) == 2
        
        # Verify the content of each row
        assert rows[0] == {'name': 'Item1', 'price': '100'}
        assert rows[1] == {'name': 'Item2', 'price': '200'}
