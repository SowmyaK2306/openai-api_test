OpenAI API Starter with Python
This is a simple Python script that uses the OpenAI API to send prompts and receive responses from GPT models.
Install requirements
pip install openai python-dotenv
Create a .env file
In the root of the project, create a file called .env with this content
OPENAI_API_KEY=your_api_key_here
Now run the script - python3 untitled.py


Notes
Uses OpenAI Python SDK v1+
Do not share your .env file publicly

Why .env Is Important
Your OpenAI API key is sensitive — it's like a password. You should never:

Hard-code it into your Python files

Upload it to GitHub

Share it in public repos or notebooks

By using a .env file and python-dotenv, you:

✅ Keep secrets safe

✅ Follow real-world dev practices

✅ Can deploy your app without changing code

Feel free to fork, use, and build on this as you like. 🚀
