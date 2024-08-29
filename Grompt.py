import argparse
import os
from dotenv import load_dotenv
from pocketgroq import GroqProvider
from pocketgroq.exceptions import GroqAPIKeyMissingError, GroqAPIError

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables or use defaults
DEFAULT_MODEL = os.getenv('GROMPT_DEFAULT_MODEL', 'llama3-groq-70b-8192-tool-use-preview')
DEFAULT_TEMPERATURE = float(os.getenv('GROMPT_DEFAULT_TEMPERATURE', '0.5'))
DEFAULT_MAX_TOKENS = int(os.getenv('GROMPT_DEFAULT_MAX_TOKENS', '1024'))

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

def rephrase_prompt(prompt: str, model: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE, max_tokens: int = DEFAULT_MAX_TOKENS) -> str:
    """
    Rephrase the given prompt using the GroqProvider.
    
    Args:
        prompt (str): The original prompt to rephrase.
        model (str): The model to use for generation.
        temperature (float): The temperature for text generation.
        max_tokens (int): The maximum number of tokens to generate.
    
    Returns:
        str: The rephrased prompt.
    
    Raises:
        GroqAPIKeyMissingError: If the GROQ_API_KEY is not set.
        GroqAPIError: If an error occurs during the API call.
    """
    try:
        groq = GroqProvider()
        
        system_message = get_rephrased_user_prompt(prompt)
        
        response = groq.generate(
            prompt=system_message,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        return response.strip()
    except GroqAPIKeyMissingError:
        raise GroqAPIKeyMissingError("GROQ_API_KEY must be set in the environment or in a .env file")
    except GroqAPIError as e:
        raise GroqAPIError(f"Error calling Groq API: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Rephrase a user prompt using Groq LLM.")
    parser.add_argument("prompt", help="The user prompt to rephrase.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="The Groq model to use.")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE, help="The temperature for text generation.")
    parser.add_argument("--max_tokens", type=int, default=DEFAULT_MAX_TOKENS, help="The maximum number of tokens to generate.")
    
    args = parser.parse_args()
    
    try:
        rephrased = rephrase_prompt(args.prompt, args.model, args.temperature, args.max_tokens)
        print("Rephrased prompt:")
        print(rephrased)
    except (GroqAPIKeyMissingError, GroqAPIError) as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def test_function():
    return "Grompt module imported successfully!"

if __name__ == "__main__":
    main()