### m05/extract_net_income_gpt4o.py
# Get AMD NetIncome from amd_data.json
#
# Author: Dhilan + GitHub Copilot
# Date: Jan 10, 2026
#
# Prompt without specifics (to understand data first / select NetIncomeLoss).
# --> failed results.  Using GPT-4o.

import json

def extract_net_income(file_path):
    """
    Extracts Net Income from the AMD SEC data JSON file and prints yearly values.

    Args:
        file_path (str): Path to the JSON file containing AMD SEC data.
    """
    try:
        # Load the JSON data
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Extract Net Income data
        if 'Net Income' in data:
            net_income_data = data['Net Income']

            # Print yearly Net Income values
            print("Yearly Net Income:")
            for year, value in net_income_data.items():
                print(f"{year}: {value}")
        else:
            print("'Net Income' key not found in the JSON data.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the JSON file
    json_file_path = "amd_data.json"

    # Extract and print Net Income
    extract_net_income(json_file_path)

"""
Output:
'Net Income' key not found in the JSON data.

That can't be right!
"""
