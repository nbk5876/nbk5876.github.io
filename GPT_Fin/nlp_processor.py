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

    # Extract the Price-to-Earnings ratio from the structured data
    pe_ratio = structured_data.get('PERatio', 'N/A')
    market_capitalization = structured_data.get('MarketCapitalization', 'N/A')


    print(f"Price to Earnings ratio is {pe_ratio} for {structured_data.get('Name')}")

    # Format a message that includes the P/E ratio information from Alpha Vantage
    detailed_description = (
        f"According to Alpha Vantage, the current Price-to-Earnings ratio for {structured_data.get('Name')} is {pe_ratio}. The MarketCapitalization is {market_capitalization}."
        "Can you provide a financial analysis based on this P/E ratio?"
    )

    print(f"\nDetailed Description:\n {detailed_description} ")

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
