#------------------------------------------------------------
# data_fetcher.py
# Purpose: Fetch data from one or more financial databases
#          based on the user's query
#------------------------------------------------------------
import os
import requests
from utils import log_error
import json

def fetch_financial_data(query):
    print("Running fetch_financial_data")
    FINAGE_API_KEY = os.getenv('FINAGE_API_KEY')

    """
    Fetch financial data based on the user's query.
    This can be implemented using an API or web scraping methods.
    
    :param query: The user's financial query.
    :return: Raw financial data from the web.
    """
    # Example implementation using an API
    api_url = f"https://api.finage.co.uk/last/stock/NVDA?apikey={FINAGE_API_KEY}"
    print(f"Finage URL is {api_url}")
    try:
        response = requests.get(api_url, params={'query': query})
        response.raise_for_status()
        data = response.json()

        # Print the entire JSON response as a string for debugging
        print(json.dumps(data, indent=4))

        return data
    except requests.RequestException as e:
        log_error("Error fetching financial data: {}".format(e))
        return None
