<h1 align=center>OLX Web Scraper</h1>
<br>

<div align=center>
    <span>🍿</span>
<a href="https://www.youtube.com/watch?v=1tqYgZAPzo0" alt="Video Demo">Video Demo</a>
    <span>🍿</span>
</div>

## 🎯 Project Overview
![Python](https://img.shields.io/badge/Python-darkblue.svg?logo=python)
![Testing](https://img.shields.io/badge/Pytest-lightblue.svg?logo=Pytest)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg) <br>
Intelligent web scraping tool for **OLX marketplace** with advanced **bilingual support** (Arabic/English). Features automated **price analysis calculations**, **regex currency processing**, and **CSV export functionality** for comprehensive market research and data analysis. <br>

## 🏗️ Architecture & Design

### Tech Stack

- **Python 3.6+** → Core scripting language with robust web scraping capabilities
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

7. 📁 **CSV Data Export**  
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
```python
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

## ⚠️ Limitations & Considerations

- **Website Dependencies**: Relies on specific OLX CSS class structure
- **Rate Limiting**: No built-in delays - use responsibly to avoid IP blocking
- **Regional Support**: Optimized for Egyptian OLX with EGP currency
- **Network Dependency**: Requires stable internet connection
- **Legal Compliance**: Users must respect OLX terms of service

## 🧪 Testing

Run the included test suite:
```bash
python test_project.py
```

Test coverage includes:
- URL validation
- Price extraction accuracy  
- CSV file generation
- Error handling scenarios

## 🤝 Contributing

### How to Contribute
1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

### Development Areas
- 🌐 Support for additional OLX regions
- ⏱️ Rate limiting and request throttling
- 📊 Advanced analytics and visualization
- 🔄 Automated data refresh scheduling
- 🎨 GUI interface development

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE.txt](LICENSE.txt) file for details.

---

## ⚖️ Ethical Usage Disclaimer

This tool is designed for **educational and research purposes**. Users must:
- ✅ Respect OLX's robots.txt and terms of service
- ✅ Implement appropriate request delays for large-scale scraping  
- ✅ Use scraped data responsibly and legally
- ✅ Consider website load and server resources

*Always prioritize ethical web scraping practices and website sustainability.*
