from RPA.Browser.Selenium import Selenium
from config import CHALLENGE_URL, AGENCY_LIST
import json
import time
import csv
import pandas as pd
browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)
    dive_in = "xpath://a[contains(text(),'DIVE IN')]"
    dive_in_button = browser_lib.find_element(dive_in)
    time.sleep(1)
    dive_in_button.click()


def scrape_agency_list():
    scrape_agency_list = """
    let saved_list = {};
    function scrape_agency_list(){
    agency_list = document.querySelectorAll("div.col-sm-4.text-center.noUnderline");
    final_list ={};
    for(var i=0;i<agency_list.length; i++ ){

      agency_name = document.querySelectorAll("div.col-sm-4.text-center.noUnderline")[i].querySelector('span.h4').innerText;
      agency_expense = document.querySelectorAll("div.col-sm-4.text-center.noUnderline")[i].querySelector('span.h1').innerText;
      agency_link = document.querySelectorAll('a.btn.btn-default.btn-sm')[0].href;
      final_list[i] = {agency_name: agency_name, agency_expense: agency_expense, agency_link: agency_link };

    }
      return final_list;
    }
    saved_list = scrape_agency_list();
    data = "<div id='agency_data'>" + JSON.stringify(saved_list) + "</div>";
    console.log(data);
    document.write(data);
    """
    browser_lib.execute_javascript(scrape_agency_list)
    time.sleep(3)
    data = browser_lib.find_element('agency_data')
    data = json.loads(data.text)
    print(data)
    with open(AGENCY_LIST, 'w') as csv_data:
        column_names = ["Agency Name", "Agency Expense", "Agency Link"]
        csv_writer = csv.writer(csv_data, delimiter=',')
        csv_writer.writerow(column_names)
        for k, v in data.items():
            data_row = dict(v)
            print([v['agency_name'], v['agency_expense'], v['agency_link']])
            data_row = [v['agency_name'], v['agency_expense'], v['agency_link']]
            csv_writer.writerow(data_row)
    browser_lib.close_all_browsers()

# def scrape_agency_investments(AGENCY_LIST):
#     agency_list = pd.read_csv(AGENCY_LIST)
#     for agency in agency_list['Agency Link']:
#         print(agency)
#         scrape_investment_from_link(agency)
#
# def scrape_investment_from_link(agency):
#     browser_lib.open_available_browser(agency)
#     time.sleep(15)
#     investment_list_selector = browser_lib.find_element('select.form-control.c-select')
#     browser_lib.select_from_list_by_value("-1", locator=investment_list_selector)

# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website(CHALLENGE_URL)
        scrape_agency_list()
        # scrape_agency_investments(AGENCY_LIST)

    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
