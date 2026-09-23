### Get AMD Revenue
### m02a-instructor/get_amd_revenue_gpt4o.py
###
### Author: Dhilan + GitHub Copilot
### Date: Jan 10, 2026
###
### Vague prompt, failed results.  Using GPT-4o.

import json

def get_amd_revenue(json_file):
    """
    Extracts AMD's revenue from the given JSON file.

    Args:
        json_file (str): Path to the JSON file containing AMD data.

    Returns:
        float: AMD's revenue if found, otherwise None.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Assuming the JSON structure contains a key 'revenue' for AMD's revenue
        revenue = data.get('revenue')

        if revenue is not None:
            print(f"AMD's Revenue: ${revenue}")
            return revenue
        else:
            print("Revenue data not found in the JSON file.")
            return None

    except FileNotFoundError:
        print(f"Error: The file {json_file} does not exist.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")
        return None

if __name__ == "__main__":
    # Replace 'amd_data.json' with the path to your JSON file
    json_file_path = 'amd_data.json'
    get_amd_revenue(json_file_path)


"""
Output:
Revenue data not found in the JSON file.

Needed to use `RevenueFromContractWithCustomerExcludingAssessedTax`
"""
