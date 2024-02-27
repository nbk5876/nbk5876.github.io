#------------------------------------------------------------
# fin_gpt_main.py
# Purpose: This is the main script of the FinGPT prototype
#          which is intended to assist in the analysis of 
#          stock market equities
# Author: T Byorick 2024
#------------------------------------------------------------
print("Running fin_gpt_main.py")
from data_fetcher import fetch_financial_data
from data_structurer import structure_data
from nlp_processor import process_query
from cache_manager import CacheManager
import utils

def main():
    #user_query = input("Enter your financial query: ")
    user_query = "What is the Price-to-Earnings ratio for Microsoft?"
    print(user_query)

    data = fetch_financial_data(user_query)

    structured_data = structure_data(data)

    #cache_manager = CacheManager()
    #cached_data = cache_manager.get_cached_data(structured_data)
    
    #if not cached_data:
    response = process_query(user_query, structured_data)
    #   cache_manager.cache_data(structured_data)
    #else:
    #    response = cached_data
    
    print(response)

if __name__ == "__main__":
    main()
