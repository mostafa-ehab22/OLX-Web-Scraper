 <div align=center>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Harvard_University_coat_of_arms.svg/800px-Harvard_University_coat_of_arms.svg.png" height=215>
    <p>2024</p>
</div>

<div align=center>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://cs50.harvard.edu/python/2022/">Course</a> | 
    <a href="https://www.youtube.com/watch?v=1tqYgZAPzo0" alt="Video Demo">Video Demo</a> | 
    <a href="https://certificates.cs50.io/cf88d045-083e-4ee7-b51c-d5b447ea86dd.png?size=A4">Certification</a>
</div>
 

## 🎯 Project Overview
![Python](https://img.shields.io/badge/Python-darkblue.svg?logo=python)
![Testing](https://img.shields.io/badge/Pytest-lightblue.svg?logo=Pytest) <br>
Intelligent web scraping tool developed as the final project for **Harvard's CS50 Introduction to Programming with Python**, targeting the **OLX marketplace** with seamless **bilingual support** (Arabic/English). Delivers automated **price analysis calculations**, **regex currency processing**, and **CSV export functionality** for comprehensive market research and data analysis. <br>

## 🏗️ Architecture & Design

### Tech Stack

- **Python** → Core scripting language with robust web scraping capabilities
- **Pytest** → Testing framework with mocking, fixtures, and coverage analysis
- **Requests** → HTTP library for fetching web content
- **BeautifulSoup4** → HTML parsing and DOM navigation
- **CSV Module** → Data export with UTF-8 encoding support
- **Regex** → Advanced currency extraction and price processing


### Core Components

- **🌐 Web Fetching ```(fetch_listings)```:**<br>
Retrieves and parses OLX listing pages using requests and BeautifulSoup.<br>
Handles network errors and HTML structure variations gracefully.

- **💰 Price Processing ```(add_item_price)```:**<br>
Advanced regex-based currency extraction supporting Arabic/English formats.<br>
Cleans and normalizes price data for accurate calculations.

- **📊 Analytics Engine ```(evaluate_prices)```:**<br>
Statistical analysis calculating lowest and average prices from extracted data.<br>
Provides comprehensive market insights with error handling.

- **📁 CSV Export ```(create_csv)```:**<br>
UTF-8 encoded file generation supporting bilingual content.<br>
Structured data output for further analysis and reporting.

### Data Processing Flow
```
User Input → Web Scraping → Data Extraction → Price Analysis → CSV Export
├── 🔗 URL Collection → Get OLX listing page
├── 🔨 HTML Parsing → Extract item containers  
├── 💵 Price Cleaning → Regex currency processing
├── 📈 Statistics → Min/max/average calculations
└── 💾 Export → UTF-8 CSV with bilingual support
```

### Benefits:

- ✅ **Bilingual Support** - Handles Arabic and English content seamlessly
- ✅ **Smart Parsing** - Regex-based price extraction with error handling
- ✅ **Market Analysis** - Automatic price statistics and insights
- ✅ **Data Export** - Clean CSV output for further analysis

## ⚙️ Features

1. 🔗 **Interactive URL Input**  
   User-friendly prompts for OLX listing URLs with validation.

2. 📂 **Flexible File Paths**  
   Configurable output locations with default fallback to Documents folder.

3. 🕷️ **Robust Web Scraping**  
   BeautifulSoup-powered HTML parsing targeting specific OLX CSS classes.

4. 🏷️ **Bilingual Item Names**  
   Extracts Arabic and English product titles with fallback handling.

5. 💰 **Smart Price Extraction**  
   Regex-based currency processing supporting various EGP formats.

6. 📊 **Price Analytics**  
   Real-time calculation of minimum and average prices across listings.

7. 📤 **CSV Data Export**  
   UTF-8 encoded file generation with structured headers and clean formatting.

8. ⚠️ **Error Handling**  
   Comprehensive exception management for network, parsing, and file operations.

## 📂 Project Structure
```
OLX-Web-Scraper/
│
├── 📄 project.py                         ⬅️ Main scraper application
├── 🧪 test_project.py                    ⬅️ Unit tests and validation
├── 📋 README.md                          ⬅️ Project documentation  
├── 📜 LICENSE.txt                        ⬅️ MIT License
├── 🖼️ Diagram.png                        ⬅️ Visual project overview
├── 📐 diagram.drawio                     ⬅️ Editable diagram source
└── 📁 __pycache__/                       ⬅️ Python cache files
```

## 🔧 Installation & Setup

### Prerequisites
```bash
Python 3.6+ installed
pip package manager
Stable internet connection
```

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/mostafa-ehab22/OLX-Web-Scraper.git
cd OLX-Web-Scraper

# Install dependencies
pip install requests beautifulsoup4
```

### Running the Scraper
```bash
python project.py
```

## 💻 Usage Examples

### Basic Usage Flow
```bash
$ python project.py

Item link: https://olx.com.eg/items/q-iphone
Save folder path (Default: Documents\output.csv): 

iPhone 13 Pro Max 256GB : 28,500 EGP
iPhone 12 Pro 128GB : 22,000 EGP  
iPhone 11 64GB : 15,500 EGP
Samsung Galaxy S23 Ultra : 35,000 EGP

(Showing 4 results)

Lowest Price: 15,500.00 EGP
Average Price: 25,250.00 EGP

Do you want to create csv file? (y/n): y
File created successfully!
```

### Advanced Configuration
```bash
# Custom save path example
Item link: https://olx.com.eg/items/q-laptop
Save folder path: /Users/username/Desktop/laptop_prices.csv
```

## 💻 Code Highlights

### Smart Price Processing
```python
def add_item_price(item_price, prices):
    if item_price != "Price not found":
        try:
            # Regex to extract numeric part of the price
            match = re.search(r'\d+[\.,\d]*', item_price)
            if match:
                # Replace commas & convert to float
                clean_price_str = match.group().replace(",", "")
                clean_price = float(clean_price_str)
                prices.append(clean_price)
        except ValueError:
            pass  # Graceful handling of invalid price formats
```

### Robust Web Scraping
```python
def fetch_listings(link):
    page = requests.get(link)
    src = page.content # Page content (Byte code)
    soup = BeautifulSoup(src, "html.parser") # Parsing page
    
    # Target specific OLX CSS classes for reliable extraction
    listings = soup.find_all('div', {'class': 'b5af0448'})
    return listings
```

### Bilingual CSV Export
```python
def create_csv(items_details, save_folder):
    headers = items_details[0].keys()
    
    # UTF-8 encoding ensures Arabic text support
    with open(save_folder, 'w', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, headers)
        writer.writeheader()
        writer.writerows(items_details)
        print("File created successfully!\n")
```

## 🎛️ Configuration

### Supported OLX Regions
- 🇪🇬 Egypt (olx.com.eg)
- 🌍 Other Arabic-speaking regions with similar structure

### CSS Selectors Used
```python
# Item containers
listings = soup.find_all('div', {'class': 'b5af0448'})

# Product names  
item_name_tag = listings[i].find('h2', {'class': '_941ffa5e'})

# Price information
item_price_tag = listings[i].find('span', {'class': '_1f2a2b47'})
```

## ⚠️ Limitations

- **Website Dependencies**: Relies on specific OLX CSS class structure
- **Rate Limiting**: No built-in delays - use responsibly to avoid IP blocking
- **Regional Support**: Optimized for Egyptian OLX with EGP currency
- **Network Dependency**: Requires stable internet connection
- **Legal Compliance**: Users must respect OLX terms of service

---
# 🧪 Quality Assurance

Comprehensive **pytest** test suite ensuring reliable web scraping operations with **unit testing**, **data validation**, and **error handling scenarios**.

## 🎯 Test Suite Overview

### Running the Test Suite
```bash
#Run the complete test suite
python test_project.py

# Run all tests with verbose output
pytest test_project.py -v

# Run tests with coverage report
pytest test_project.py --cov=project

# Run specific test function
pytest test_project.py::test_add_item_price -v
```

### Testing Categories & Coverage

**1. 🔗 Input Validation & User Interface Tests**
```python
def test_get_info(monkeypatch):
    # Test with user providing both link & save folder
    input_values = iter(["http://example.com", "custom_folder/output.csv"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    assert get_info() == ("http://example.com", "custom_folder/output.csv")
    
    # Test with user providing no link (should trigger SystemExit)
    monkeypatch.setattr('builtins.input', lambda _: "")
    with pytest.raises(SystemExit):
        get_info()
```
**2. 🔨 Web Scraping & HTML Parsing Tests**
```python
def test_fetch_listings(monkeypatch):
    # Define a mock response class to simulate HTTP response
    class MockResponse:
        @property
        def content(self):
            # Simulate HTML content with a byte string
            return b'<div class="b5af0448">Listing</div>' 
        
    # Using monkeypatch: Replace requests.get with lambda function => Returns MockResponse instance
    monkeypatch.setattr(requests, 'get', lambda _: MockResponse())
    
    # Call fetch_listings with a test URL
    listings = fetch_listings("http://example.com")
    
    # Assert that exactly one listing was found
    assert len(listings) == 1
    
    # Assert that the text content of the first listing matches "Listing"
    assert listings[0].text == "Listing"
```

**3. 💰 Price Processing & Data Validation Tests**
```python
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
```

**4. 📁 CSV Generation & File I/O Tests**
```python
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
```

## 📊 Implementation Details

### Testing Techniques Used:
- 🔧 Monkeypatching: Used ``pytest.monkeypatch`` to mock user input and HTTP requests safely
- 🗂️ Temporary Files: Utilized ``tmp_path`` fixture for clean file testing without side effects
- 🎭 Mock Objects: Created custom ``MockResponse`` class to simulate web requests
- ⚠️ Exception Testing: Used ``pytest.raises()`` to validate proper error handling
- 📋 Iterators: Implemented input value iteration for multi-step user interaction testing

### Quality Assurance Coverage:

- ✅ Input Validation: Both valid inputs and edge cases (empty strings)
- ✅ Web Request Mocking: Safe testing without external dependencies
- ✅ Price Processing: Numeric conversion and invalid data handling
- ✅ Statistical Functions: Mathematical accuracy verification
- ✅ File Operations: CSV generation with UTF-8 encoding validation
- ✅ Error Scenarios: SystemExit and None return value testing

## 🤝 Contributing

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Areas
- 🌐 Support for additional OLX regions
- ⏱️ Rate limiting and request throttling
- 📊 Advanced analytics and visualization
- 🔄 Automated data refresh scheduling
- 🎨 GUI interface development

## ⚖️ Ethical Usage Disclaimer

This tool is designed for **educational and research purposes**. Users must:
- ✅ Respect OLX's terms of service
- ✅ Implement appropriate request delays for large-scale scraping  
- ✅ Use scraped data responsibly and legally
- ✅ Consider website load and server resources

*Always prioritize ethical web scraping practices and website sustainability.*

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE.txt](LICENSE.txt) file for details.
