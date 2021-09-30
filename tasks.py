from RPA.Browser.Selenium import Selenium

# Preparing Assets & Required Resources
browser_lib = Selenium()
challenge_website_url = ""
agency_website_url = ""


# Task 1 - Download List Of Agency
def download_agency_list():
    """Downloads List Of Agency"""
    agency_list = scrape_agency_list(challenge_website_url)
    save_agency_list(agency_list)

def scrape_agency_list(challenge_website_url):
    """Scrapes List Of Agencies"""

def save_agency_list():
    """Save List Of Agency"""

# Task 2 - Download Individual Investments & Business Cases
def download_individual_investments():
    investment_list = scrape_investment_list(agency_website_url)
    download_business_case(investment_list)
    save_investment_list(investment_list)

def scrape_investment_list(agency_website_url):
    """Scrape List of Individual Investments From Table"""

def download_business_case(investment_list):
    """Download Business Cases From Investment List"""

def save_investment_list(investment_list):
    """Save Investments To An Excel File"""

# Define a main() function that calls the other functions in order:
def main():
    try:
        download_agency_list()
        download_individual_investments()
    finally:
        browser_lib.close_all_browsers()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
