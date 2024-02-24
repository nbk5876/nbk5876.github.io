# test_openai_v3.py
import os
import openai

print("####################################")
print("Running: test_openai_v2.py")

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

# Explicitly set the API key for OpenAI
openai.api_key = api_key

try:
    # Create a chat completion request using the direct openai function call
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate the following English text to French:"},
            {"role": "user", "content": "Hello, world!"}
        ]
    )

    # Print the completion result
    print(completion.choices[0].message['content'])
except Exception as e:
    print(f"An error occurred: {e}")
