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
    ebitda = structured_data["overview"].get("EBITDA")
    operating_margin_ttm = structured_data["overview"].get("OperatingMarginTTM")
    return_on_equity_ttm = structured_data["overview"].get("ReturnOnEquityTTM")
    beta = structured_data["overview"].get("Beta")
    book_value = structured_data["overview"].get("BookValue")
    ev_to_ebitda = structured_data["overview"].get("EVToEBITDA")
    gross_profit_ttm = structured_data["overview"].get("GrossProfitTTM")
    earnings_per_share = structured_data["overview"].get("EPS")


    """ TODO 3/2/24 Add these metrics to be extracted from alpha vantage JSON
    Sector and Industry - Helps in understanding the company's operating environment and for sector-specific analysis.

    RevenueTTM (Trailing Twelve Months) - Gives insight into the company's sales and size over the most recent 12-month period.

    OperatingMarginTTM (Trailing Twelve Months) - Reflects the proportion of a company's revenue left over after paying for variable costs of production, a key indicator of operational efficiency.

    ReturnOnEquityTTM (Trailing Twelve Months) - Measures a corporation's profitability by revealing how much profit a company generates with the money shareholders have invested. It's a measure of financial performance.

    DividendYield - Shows how much a company pays out in dividends each year relative to its stock price, important for income-focused investors.

    Beta - Measures the volatility of a stock's returns relative to the overall market, essential for risk assessment.

    52WeekHigh and 52WeekLow - Provides a sense of the stock's recent trading range, which can be useful for technical analysis and understanding market sentiment.

    AnalystRatingStrongBuy, AnalystRatingBuy, AnalystRatingHold, AnalystRatingSell, AnalystRatingStrongSell - Offers a consensus view from analysts on the stock's prospects, which can be useful for understanding market expectations.

    BookValue - Represents the net asset value of the company according to its books, useful for valuation comparisons.

    EVToEBITDA (Enterprise Value to EBITDA) - A valuation metric that compares the value of a company, including debt and liabilities, to its actual earnings before interest, taxes, depreciation, and amortization. This can provide a clearer picture of a company's financial health and valuation compared to P/E ratio alone.

    GrossProfitTTM (Trailing Twelve Months) - Indicates the company's total sales revenue minus its cost of goods sold, an important metric for assessing a company's financial health and operational efficiency.
    """

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
    #detailed_description = (f"According to Alpha Vantage (https://www.alphavantage.co/), the current Price-to-Earnings ratio for {company_name} is {pe_ratio}. Profit Margin is {profit_margin}. Market Capitalization is {market_cap}. The current stock price is {current_price} and the target price is {target_price}. Earnings per share is {earnings_per_share}. EBITDA is {ebitda} " . "    Here are more metrics for {company_name}.  Operating Margin TTM is {operating_margin_ttm},     ReturnOnEquityTTM is {return_on_equity_ttm},     Beta is {beta},     Book Value is {book_value},     EV To EBITDA is {evt_to_ebitda},     GrossProfitTTMis {gross_profit_ttm}" . "Can you provide a financial analysis based on these data points? Are there areas where the company is struggling?"
    #)

    # Format a message that includes the P/E ratio information from Alpha Vantage
    detailed_description = (
        f"According to Alpha Vantage (https://www.alphavantage.co/), the current Price-to-Earnings ratio for {company_name} is {pe_ratio}. Profit Margin is {profit_margin}. Market Capitalization is {market_cap}. The current stock price is {current_price} and the target price is {target_price}. Earnings per share is {earnings_per_share}. EBITDA is {ebitda}. "
        + f"Here are more metrics for {company_name}. Operating Margin TTM is {operating_margin_ttm}, ReturnOnEquityTTM is {return_on_equity_ttm}, Beta is {beta}, Book Value is {book_value}, EV To EBITDA is {ev_to_ebitda}, GrossProfitTTM is {gross_profit_ttm}. "
        + "Can you provide a financial analysis based on these data points? Are there areas where the company is struggling?"
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
