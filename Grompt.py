import argparse
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables or use defaults
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
DEFAULT_MODEL = os.getenv('GROMPT_DEFAULT_MODEL', 'llama3-groq-70b-8192-tool-use-preview')
DEFAULT_TEMPERATURE = float(os.getenv('GROMPT_DEFAULT_TEMPERATURE', '0.5'))
DEFAULT_MAX_TOKENS = int(os.getenv('GROMPT_DEFAULT_MAX_TOKENS', '1024'))

if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY must be set in the environment or in a .env file")

def get_rephrased_user_prompt(user_request):
    return f"""You are a professional prompt engineer. Your task is to optimize the following user request into a well-structured, clear, and effective prompt. 
    **Objective:** Clearly define the purpose or goal of the prompt to ensure the model understands the task's ultimate objective.
    The optimized prompt must meet the following criteria:
    1. **Clarity:** Ensure the prompt is easy to understand with no ambiguity.
    2. **Specific Instructions:** Include detailed and actionable steps.
    3. **Context:** Provide any necessary background information.
    4. **Structure:** Organize the prompt logically, ensuring a smooth flow of ideas.
    5. **Language:** Use concise and precise wording.
    6. **Examples:** Where applicable, include examples to illustrate the expected output.
    7. **Constraints:** Specify any limits or boundaries that must be adhered to.
    8. **Engagement:** Make the prompt engaging to maintain the user's interest.
    9. **Feedback:** Suggest ways to refine or iterate on the response if needed.
    10. **Error Handling:** Include strategies for dealing with incomplete or poorly formed input. Suggest clarifications or make reasonable assumptions where necessary.
    11. **Adaptive Flexibility:** Adapt the response style to suit the nature of the request, whether technical, creative, or otherwise.
    12. **Bias Mitigation:** Ensure the prompt avoids stereotypes and minimizes bias, promoting inclusivity and fairness.
    13. **Output Format:** Clearly specify the desired format for the response when applicable.
    14. **Step-by-Step Thinking:** Break down complex tasks into clear, sequential steps to enhance reasoning and problem-solving.
    15. **Knowledge Activation:** Prime the model with relevant domain knowledge or context when the task requires specific expertise.
    16. **Meta-Cognitive Prompts:** Encourage the model to explain its reasoning or thought process for more reliable and traceable outputs.
    17. **Ethical Considerations:** Address potential ethical implications or biases beyond simple mitigation, considering broader impacts.
    18. **Creativity and Innovation:** Foster creative and innovative thinking when appropriate for the task at hand.

    **Iterative Refinement Loop:**
    - After generating the initial rephrased prompt, critically evaluate it against each of the above criteria.
    - For each criterion, ask: "How well does the prompt meet this requirement, and how can it be improved?"
    - Consider potential edge cases or misinterpretations, and refine the prompt to address these.
    - Assess if the prompt balances specificity with flexibility, allowing for creative solutions while maintaining focus.
    - Refine the prompt iteratively until it aligns perfectly with all outlined goals and criteria.

    Remember to:
    - Clarify any ambiguities in the original request.
    - Break down complex tasks into simpler, manageable steps.
    - Provide essential context for better understanding, especially for domain-specific tasks.
    - Use precise and concise language while maintaining engagement.
    - Include relevant examples to illustrate expected inputs and outputs.
    - Define any constraints clearly, including ethical and practical boundaries.
    - Encourage critical thinking and explanation of reasoning where appropriate.

    **Do not** respond to these instructions or the original user request. 
    **Only** return the rephrased prompt, ensuring it is ready for use without additional context.
    User request: "{user_request}"
    Rephrased:
    """

def rephrase_prompt(prompt, model=DEFAULT_MODEL, temperature=DEFAULT_TEMPERATURE, max_tokens=DEFAULT_MAX_TOKENS):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY must be set in the environment or in a .env file")

    client = Groq(api_key=GROQ_API_KEY)
    
    messages = [
        {
            "role": "system",
            "content": "You are a professional prompt engineer, expert at rephrasing and optimizing prompts."
        },
        {
            "role": "user",
            "content": get_rephrased_user_prompt(prompt)
        }
    ]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Rephrase a user prompt using Groq LLM.")
    parser.add_argument("prompt", help="The user prompt to rephrase.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="The Groq model to use.")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE, help="The temperature for text generation.")
    parser.add_argument("--max_tokens", type=int, default=DEFAULT_MAX_TOKENS, help="The maximum number of tokens to generate.")
    
    args = parser.parse_args()
    
    rephrased = rephrase_prompt(args.prompt, args.model, args.temperature, args.max_tokens)
    
    if rephrased:
        print("Rephrased prompt:")
        print(rephrased)
    else:
        print("Failed to rephrase the prompt.")

if __name__ == "__main__":
    main()