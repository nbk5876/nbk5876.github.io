#------------------------------------------------------------
# nlp_processor.py
# Purpose:  The primary purpose of this script is to interpret 
#           user queries, extract relevant financial terms and 
#           concepts, and prepare them for processing to 
#           retrieve or calculate the requested financial data.
#------------------------------------------------------------
from openai import OpenAI

def process_query(user_query, structured_data):
    """
    Processes the user's financial query using OpenAI's API.

    :param user_query: The user's query as a string.
    :param structured_data: The structured data related to the financial query.
    :return: The processed response from OpenAI.
    """
    # Initialize the OpenAI client
    client = OpenAI()
    
    print("Running process_query()")
    print(user_query)
    print(structured_data)

    # Extract required information from structured_data
    company_name = structured_data["overview"].get("Name")
    pe_ratio = structured_data["overview"].get("PERatio")
    market_cap = structured_data["overview"].get("MarketCapitalization")
    target_price = structured_data["overview"].get("AnalystTargetPrice")
    profit_margin = structured_data["overview"].get("ProfitMargin")

    current_price = structured_data["currentPrice"]

    print(f"Price to Earnings ratio is {pe_ratio} for {structured_data.get('Name')}")

    """ --------------------------------------------------------------------------
    Next Steps: (Done Feb 28)
    - Need to implement some method to use the return values of two separate 
      API's to obtain financial information
      about a company.  The pe_ratio and market_capitalization values are returned by 
      query?function=OVERVIEW&symbol=MSFT and current stock price is returned by
      query?function=GLOBAL_QUOTE
      -----------------------------------------------------------------------------
    """

    # Format a message that includes the P/E ratio information from Alpha Vantage
    detailed_description = (f"According to Alpha Vantage (https://www.alphavantage.co/), the current Price-to-Earnings ratio for {company_name} is {pe_ratio}. Profit Margin is {profit_margin}. Market Capitalization is {market_cap}. The current stock price is {current_price} and the target price is {target_price}. "
        "Can you provide a financial analysis based on these data points? Are there areas where the company is struggling?"
    )

    print(f"\nEnriched User Query:\n{detailed_description} ")

    # Here, adapt the messages to fit the context of your application.
    # For a financial query, you might want to include the structured_data in some way,
    # or just pass the query directly if the structured_data isn't needed here.
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that provides financial analysis."},
            {"role": "user", "content": detailed_description}
        ]
    )

    # Assuming the response structure matches your test case,
    # adjust if the actual response format differs.
    try:
        response = completion.choices[0].message  # Adjust based on actual response structure
    except IndexError:
        response = "An error occurred processing the query."

    return response
