# gpt_bot.py
import os
from openai import OpenAI
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up OpenAI API key
api_key = os.getenv('')
"""


if not api_key:
    raise ValueError("OpenAI API key not set. Please set the OPENAI_API_KEY environment variable.")
"""
client = OpenAI(api_key=api_key)

# Function to call the external API for Python resources
def get_python_resources():
    try:
        response = requests.get('http://127.0.0.1:5001/api/learn_python')
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get('resources', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Python resources: {e}")
        return []

# Function to handle GPT-3 response
def generate_response(user_input):
    if "learn python" in user_input.lower():
        resources = get_python_resources()
        if resources:
            resources_text = "\n".join([f"{resource['title']}: {resource['url']}" for resource in resources])
            response_text = f"Here are some resources to help you learn Python:\n{resources_text}"
        else:
            response_text = "I couldn't fetch the Python resources at the moment. Please try again later."
    else:
        try:
            # This part uses GPT-3 to generate a response
            print("Making request to OpenAI API...")
            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",  # Use the model parameter
                prompt=user_input,
                max_tokens=150
            )
            print("Response received from OpenAI API")
            response_text = response.choices[0].text.strip()
        except Exception as e:
            print(f"Error making request to OpenAI: {e}")
            response_text = "Sorry, I couldn't process your request at the moment. Please try again later."
    return response_text

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({"response": "Please provide a valid message."}), 400

    response_text = generate_response(user_input)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(port=5000)
