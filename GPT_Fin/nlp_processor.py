# nlp_processor.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
client = openai.OpenAI()

def process_query(user_message):
    """
    Process the natural language query using OpenAI's GPT-4 model.

    :param user_message: The user's natural language query.
    :return: A response from the GPT-4 model that answers the user's query.
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        return completion.choices[0].message.content
    except openai.error.OpenAIError as e:
        print(f"Error processing the NLP query: {e}")
        return "I'm sorry, I couldn't process your query."

# Example usage
if __name__ == "__main__":
    user_input = "Translate the following English text to French: 'Hello, world!'"
    print(process_query(user_input))
