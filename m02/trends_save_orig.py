### Scrape Google Trends data and save it to a CSV file (with bot detection)
### m01e/trends_save.py
###
### Author: Dhilan + GitHub Copilot + Mike
### Date: November 11, 2025
###
### Based on scrape_save.py but using the enhanced trends_scraper with bot detection
import csv
from trends_scraper import get_driver, scrape_interest_data


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

    # Save data to a CSV file
    fname = 'scraped_data.csv'
    with open(fname, 'w') as fd:
        writer = csv.DictWriter(fd, fieldnames=['Region', 'Interest'])
        writer.writeheader()
        for region, interest in interest_data.items():
            writer.writerow({'Region': region, 'Interest': interest})
    print(f"Saved data to {fname}")

    driver.quit()


if __name__ == "__main__":
    main()
