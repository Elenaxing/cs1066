### Scrape Google Trends data for a given query and date range
### harvardvibecoding/m01b/scrape.py
### 
### Author: Sharon Zhou and Mike Smith
### Date: 20250916
###
### Original idea and code from https://brightdata.com/blog/web-data/how-to-scrape-google-trends

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

def get_driver():
    """
    Create and configure a Chrome WebDriver instance for web automation.
    
    This function sets up a Chrome browser instance with custom binary location
    and returns a configured WebDriver object ready for use in web scraping
    or automation tasks.
    
    Returns:
        webdriver.Chrome: A configured Chrome WebDriver instance with:
            - Custom Chrome binary location set to the local Chrome installation
            - Options configured for automation
    
    Note:
        The Chrome binary path is hardcoded for macOS. Modify CHROME_PATH
        if running on a different operating system or Chrome installation.
        
    Example:
        >>> driver = get_driver()
        >>> driver.get("https://example.com")
        >>> driver.quit()
    """
    # Update the path to the location of your Chrome binary
    CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    options = Options()
    options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(options=options)

    return driver


def get_raw_trends_data(driver, url):
    """
    Navigate to the provided URL and return the page source.

    It handles the initial 429 error, and then it waits for the user to
    handle any other errors (e.g., are-you-a-robot queries). Recently, I've
    had to deal with "something-went-wrong" errors, which are cleared by
    refreshing the page.
    
    Args:
        driver: webdriver.Chrome instance
        url: str, the URL to navigate to
    
    Returns:
        str: The page source of the loaded page
    """
    # Let the user know the URL used
    print(f"Getting data from {url}")

    # First `get` causes a 429 error, which we ignore
    driver.get(url)

    # Hopefully the second `get` works, but we wait
    # for the user to let us know when we can continue.
    driver.get(url)
    input("Press Enter to continue...")

    return driver.page_source


def extract_interest_by_sub_region(content):
    """
    Extract interest data by sub-region from Google Trends HTML content.
    
    This function parses the HTML content from a Google Trends page and extracts
    the interest percentages for different sub-regions (e.g., states, provinces)
    within the specified geographic area.
    
    Args:
        content (str): The HTML page source from a Google Trends results page
                       containing sub-region interest data
    
    Returns:
        dict: A dictionary mapping region names to their interest percentages.
              Keys are region names (e.g., "California", "Texas") and values
              are interest percentages as strings (e.g., "100", "85")
    
    Note:
        This function specifically looks for the geo-widget-wrapper with
        geo-resolution-subregion class, which contains the sub-region data
        on Google Trends pages.
        
    Example:
        >>> content = "<html>...</html>"  # Google Trends page source
        >>> data = extract_interest_by_sub_region(content)
        >>> print(data)
        {'California': '100', 'Texas': '85', 'Florida': '72'}
    """
    soup = BeautifulSoup(content, "html.parser")

    interest_by_subregion = soup.find("div", class_="geo-widget-wrapper geo-resolution-subregion")

    related_queries = interest_by_subregion.find_all("div", class_="fe-atoms-generic-content-container")

    # Dictionary to store the extracted data
    interest_data = {}

    # Extract the region name and interest percentage
    for query in related_queries:
        items = query.find_all("div", class_="item")
        for item in items:
            region = item.find("div", class_="label-text").text.strip()
            interest = item.find("div", class_="progress-value").text.strip()
            interest_data[region] = interest

    return interest_data


def scrape_interest_data(driver, url):
    """
    Scrape comprehensive interest data by sub-region from Google Trends.
    
    This function navigates to a Google Trends URL, extracts interest data from
    the initial page, and then automatically paginates through all available
    sub-region data by clicking the "Next" button until no more data is available.
    
    Args:
        driver (webdriver.Chrome): A configured Chrome WebDriver instance
        url (str): The Google Trends URL to scrape, containing query parameters
                   for date range, geographic area, and search terms
    
    Returns:
        dict: A comprehensive dictionary mapping all sub-region names to their
              interest percentages. Keys are region names (e.g., "California", 
              "Texas") and values are interest percentages as strings (e.g., 
              "100", "85"). This includes data from all paginated results.
    
    Note:
        This function handles pagination automatically by:
        1. Extracting data from the initial page
        2. Looking for and clicking the "Next" button in the geo-widget
        3. Continuing until the button is disabled or an exception occurs
        4. Accumulating all data into a single dictionary
        
        The function includes error handling for cases where pagination
        elements are not found or become unavailable.
    """
    # Navigate to the URL and grab the page's source code
    content = get_raw_trends_data(driver, url)

    # Extract the interest by sub-region (first page)
    interest_data = extract_interest_by_sub_region(content)

    # Get paginated interest data
    while True:
        # Click the md-button to load more data if available
        try:
            geo_widget = driver.find_element(
                By.CSS_SELECTOR, "div.geo-widget-wrapper.geo-resolution-subregion"
            )

            # Find the load more button with class name "md-button" and aria-label "Next"
            load_more_button = geo_widget.find_element(
                By.CSS_SELECTOR, "button.md-button[aria-label='Next']"
            )

            icon = load_more_button.find_element(By.CSS_SELECTOR, ".material-icons")

            # Check if the button is disabled by checking class-name includes arrow-right-disabled
            if "arrow-right-disabled" in icon.get_attribute("class"):
                break  # No more data to load

            load_more_button.click()
            time.sleep(1)

            # Extract the interest by sub-region (next page)
            extracted_data = extract_interest_by_sub_region(driver.page_source)
            interest_data.update(extracted_data)

        except Exception as e:
            print("Unexpected exception:", e)
            break

    return interest_data


def main():
    # Build the URL for Google Trends. This is the page we'll scrape.
    date_range = "now%207-d"
    geo = "US"
    query = "vibe coding"
    site = "https://trends.google.com/trends/explore"
    url = f"{site}?date={date_range}&geo={geo}&q={query}&hl=en"

    # Build a driver for a browser
    driver = get_driver()

    # Scrape the interest data
    interest_data = scrape_interest_data(driver, url)

    # Print these data to the console
    for region, interest in interest_data.items():
        print(f"{region}: {interest}")

    driver.quit()

if __name__ == "__main__":
    main()
