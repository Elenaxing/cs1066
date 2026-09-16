### Plot the scraped and saved Google Trends data
### m01e/trends_plot.py
### 
### Author: Sharon Zhou and Mike Smith
### Date: 20250916
###
### Original idea and code from https://brightdata.com/blog/web-data/how-to-scrape-google-trends

import pandas as pd
import matplotlib.pyplot as plt

def main():
    input_file = 'scraped_data.csv'
    output_file = 'interest_data.png'

    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(input_file)
    print(f"Read data from {input_file}")
    print(df.head())    # Sanity check

    # Plot the data in a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Region'], df['Interest'], color='skyblue')

    # Add labels and title
    plt.xlabel('Region')
    plt.ylabel('Interest')
    plt.title('Google Trends Interest by Region')

    # Rotate the x-axis labels for readability
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig(output_file)
    print(f"Saved plot to {output_file}")

if __name__ == "__main__":
    main()