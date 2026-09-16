### Simplified Google Trends Scraper with Bot Detection
### vibe-dev/m01/trends_scraper.py
###
### Author: Dhilan + GitHub Copilot
### Date: November 11, 2025
###
### Simplified version like scrape.py but with essential bot detection features

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import random
import re


def get_driver():
    """
    Create and configure a headless Chrome WebDriver instance for web automation.
    """
    print("Setting up headless Chrome driver...")

    options = Options()
    options.add_argument("--headless=new")

    # Essential arguments for Codespaces/containers
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--window-size=1920,1080")

    # Anti-detection measures
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    try:
        driver = webdriver.Chrome(options=options)
        # Execute script to remove webdriver property
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        print("Chrome driver initialized successfully")
        return driver
    except Exception as e:
        print(f"Failed to initialize Chrome driver: {e}")
        return None


def random_delay(min_sec=2.0, max_sec=5.0):
    """Random delay to mimic human behavior"""
    delay = random.uniform(min_sec, max_sec)
    print(f"Waiting {delay:.1f}s...")
    time.sleep(delay)


def handle_bot_detection(driver):
    """Check for bot detection indicators and handle them"""
    try:
        page_source = driver.page_source.lower()

        bot_indicators = [
            "captcha",
            "verify you are human",
            "unusual traffic",
            "something went wrong",
            "rate limited",
            "try again later"
        ]

        if any(indicator in page_source for indicator in bot_indicators):
            print("Bot detection detected, attempting refresh strategy...")

            # Strategy 1: Simple refresh
            driver.refresh()
            random_delay(3, 6)

            # Strategy 2: Navigate away and back
            driver.get("https://trends.google.com")
            random_delay(2, 4)

            return True

    except Exception as e:
        print(f"Error checking for bot detection: {e}")

    return False


def extract_geo_data(driver):
    """Extract geographical interest data from the page"""
    try:
        # Look for geo widget containers
        geo_widget_selector = "div.geo-widget-wrapper.geo-resolution-subregion"
        geo_widgets = driver.find_elements(By.CSS_SELECTOR, geo_widget_selector)

        for widget in geo_widgets:
            # Look for content containers
            content_containers = widget.find_elements(
                By.CSS_SELECTOR, "div.fe-atoms-generic-content-container"
            )

            geo_data = {}
            for container in content_containers:
                items = container.find_elements(By.CSS_SELECTOR, "div.item")

                for item in items:
                    try:
                        # Extract region name and value
                        label_elem = item.find_element(By.CSS_SELECTOR, "div.label-text")
                        value_elem = item.find_element(By.CSS_SELECTOR, "div.progress-value")

                        region = label_elem.text.strip()
                        value_text = value_elem.text.strip()

                        # Convert value to string like scrape.py (but clean it up)
                        geo_data[region] = value_text

                    except Exception:
                        continue  # Skip problematic items

            if len(geo_data) >= 3:
                print(f"Found {len(geo_data)} regions via geo widget")
                return geo_data

    except Exception as e:
        print(f"Extraction error: {e}")

    return None


def scrape_interest_data(driver, url):
    """Scrape Google Trends interest data with bot detection and pagination"""
    print(f"Starting scrape for: {url}")

    max_retries = 5
    for attempt in range(max_retries):
        print(f"\nAttempt {attempt + 1}/{max_retries}")

        try:
            # Navigate to Google Trends
            driver.get(url)
            random_delay(3, 6)

            # Check for bot detection and handle it
            page_source_lower = driver.page_source.lower()
            bot_indicators = ["captcha", "verify you are human", "unusual traffic",
                            "something went wrong", "rate limited", "try again later"]

            if any(indicator in page_source_lower for indicator in bot_indicators):
                print("Bot detection detected, attempting refresh strategy...")
                # Strategy 1: Simple refresh
                driver.refresh()
                random_delay(3, 6)
                # Strategy 2: Navigate away and back
                driver.get("https://trends.google.com")
                random_delay(2, 4)
                driver.get(url)
                random_delay(3, 6)

            # Wait for page to load
            print("Waiting for page to load...")
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Extract data with pagination
            all_data = extract_geo_data(driver)
            if not all_data:
                print("No geographical data found on page")
                continue

            print(f"Initial page: Found {len(all_data)} regions")

            # Handle pagination
            page_count = 1
            max_pages = 10

            while page_count < max_pages:
                try:
                    print(f"Looking for pagination (page {page_count + 1})...")

                    # Look for geo widget container
                    geo_widget = driver.find_element(
                        By.CSS_SELECTOR, "div.geo-widget-wrapper.geo-resolution-subregion"
                    )

                    # Find Next button
                    next_button = geo_widget.find_element(
                        By.CSS_SELECTOR, "button.md-button[aria-label='Next']"
                    )

                    # Check if disabled
                    icon = next_button.find_element(By.CSS_SELECTOR, ".material-icons")
                    if "arrow-right-disabled" in icon.get_attribute("class"):
                        print("Reached last page (Next button disabled)")
                        break

                    # Click next
                    print(f"Clicking Next button for page {page_count + 1}...")
                    driver.execute_script("arguments[0].click();", next_button)

                    # Wait for new data
                    random_delay(1, 3)

                    # Extract data from this page
                    page_data = extract_geo_data(driver)
                    if page_data:
                        new_regions = len([k for k in page_data.keys() if k not in all_data])
                        all_data.update(page_data)
                        print(f"Page {page_count + 1}: Found {new_regions} new regions")

                        if new_regions == 0:
                            print("No new data found, assuming end of pagination")
                            break
                    else:
                        print(f"No data found on page {page_count + 1}")
                        break

                    page_count += 1

                except Exception as e:
                    print(f"Pagination error on page {page_count + 1}: {e}")
                    break

            if all_data:
                print(f"Total pagination result: {len(all_data)} regions across {page_count} pages")
                return all_data

        except TimeoutException:
            print("Page load timeout")
        except WebDriverException as e:
            print(f"WebDriver error: {e}")

        if attempt < max_retries - 1:
            print("Retrying in a moment...")
            random_delay(5, 10)

    print("All attempts failed")
    return {}


def main():
    # Build the URL for Google Trends
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
    if not interest_data:
        print("No interest data retrieved.")
        return

    for region, interest in interest_data.items():
        print(f"{region}: {interest}")


if __name__ == "__main__":
    main()
