# ============================================================
# WARNING: This file is specifically for the Grompt plugin.
# Do not run this server independently or use it for other purposes.
# It is designed to work exclusively with the Grompt Chrome extension.
# ============================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from pocketgroq import GroqProvider
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables or use defaults
DEFAULT_MODEL = os.getenv('GROMPT_DEFAULT_MODEL', 'llama3-groq-70b-8192-tool-use-preview')
DEFAULT_TEMPERATURE = float(os.getenv('GROMPT_DEFAULT_TEMPERATURE', '0.5'))
DEFAULT_MAX_TOKENS = int(os.getenv('GROMPT_DEFAULT_MAX_TOKENS', '4096'))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_rephrased_user_prompt(user_request: str) -> str:
    """
    Generate a system message for prompt rephrasing.
    
    Args:
        user_request (str): The original user request.
    
    Returns:
        str: A system message for prompt rephrasing.
    """
    return f"""You are a professional prompt engineer. Your task is to optimize the following user request into a well-structured, clear, and effective prompt. 
    [Rest of the system message remains unchanged]
    User request: "{user_request}"
    Rephrased:
    """

@app.route('/rephrase', methods=['POST'])
def rephrase():
    data = request.json
    prompt = data.get('prompt')
    api_key = request.headers.get('Authorization').split(' ')[1]

    groq = GroqProvider(api_key=api_key)
    try:
        system_message = get_rephrased_user_prompt(prompt)
        response = groq.generate(
            prompt=system_message,
            model=DEFAULT_MODEL,
            temperature=DEFAULT_TEMPERATURE,
            max_tokens=DEFAULT_MAX_TOKENS,
        )
        return jsonify({"rephrased": response.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)