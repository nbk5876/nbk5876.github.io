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

    # Here, adapt the messages to fit the context of your application.
    # For a financial query, you might want to include the structured_data in some way,
    # or just pass the query directly if the structured_data isn't needed here.
    completion = client.chat.completions.create(
        #model="gpt-3.5-turbo",
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Provide a detailed analysis of the following financial information:"},
            {"role": "user", "content": user_query}
            # If you have structured data to include, you might add another message here
            # {"role": "system", "content": structured_data}  # This line is just an example
        ]
    )

    # Assuming the response structure matches your test case,
    # adjust if the actual response format differs.
    try:
        response = completion.choices[0].message  # Adjust based on actual response structure
    except IndexError:
        response = "An error occurred processing the query."

    return response
