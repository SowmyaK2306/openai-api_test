import openai
from dotenv import load_dotenv
import os
 
# Load environment variables from .env file
load_dotenv()
 
# Set up the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
 
# Function to call the OpenAI API
def call_openai_llm(prompt, model="gpt-3.5-turbo", max_tokens=100):
    try:
        # Initialize the OpenAI client
        client = openai.OpenAI(api_key=openai.api_key)
        # Make the API call using the new syntax
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"OpenAI Error: {str(e)}"
 
# Example usage with multiple prompts and models
if __name__ == "__main__":
    prompts = [
        "Write a haiku about artificial intelligence.",
        "Explain neural networks in one sentence."
    ]
    models = ["gpt-3.5-turbo", "gpt-4o"]  # Available OpenAI models
 
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        for model in models:
            print(f"\nModel: {model}")
            response = call_openai_llm(prompt, model=model)
            print("Response:")
            print(response)
 