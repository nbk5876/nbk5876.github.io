# test_openai.py
import os
import openai

print("####################################")
print("Running: test_openai.py")

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

# Set the API key for OpenAI
openai.api_key = api_key
#print("KEY", api_key)

try:
    # Make a request to the OpenAI API for text completion
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Translate the following English text to French: 'Hello, world!'",
        max_tokens=60
    )
    print(response.choices[0].text.strip())
except Exception as e:
    print(f"An error occurred: {e}")
