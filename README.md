# Grompt Utility

Grompt is a Python utility that uses the Groq LLM provider service to re-engineer prompts. It's designed to optimize user prompts for better results when working with large language models.

## Features

- Rephrase and optimize user prompts using Groq's LLM services
- Configurable via environment variables or .env file
- Can be used as a module in other Python scripts or run from the command line
- Supports various Groq models and customizable parameters

## Prerequisites

- Python 3.6 or higher
- A Groq API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/jgravelle/grompt.git
   cd grompt
   ```

2. Install the required dependencies:
   ```
   pip install groq python-dotenv
   ```

3. Create a `.env` file in the project root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Configuration

You can configure Grompt using environment variables or a `.env` file. Here are the available configuration options:

- `GROQ_API_KEY`: Your Groq API key (required)
- `GROMPT_DEFAULT_MODEL`: The default Groq model to use (optional, default is 'llama3-groq-70b-8192-tool-use-preview')
- `GROMPT_DEFAULT_TEMPERATURE`: The default temperature for text generation (optional, default is 0.5)
- `GROMPT_DEFAULT_MAX_TOKENS`: The default maximum number of tokens to generate (optional, default is 1024)

Example `.env` file:

```
GROQ_API_KEY=your_api_key_here
GROMPT_DEFAULT_MODEL=llama3-groq-70b-8192-tool-use-preview
GROMPT_DEFAULT_TEMPERATURE=0.7
GROMPT_DEFAULT_MAX_TOKENS=2048
```

## Usage

### As a Command-Line Tool

Run Grompt from the command line:

```
python grompt.py "Your prompt here" [--model MODEL] [--temperature TEMP] [--max_tokens MAX_TOKENS]
```

Options:
- `--model`: Specify the Groq model to use (overrides the default)
- `--temperature`: Set the temperature for text generation (overrides the default)
- `--max_tokens`: Set the maximum number of tokens to generate (overrides the default)

Example:
```
python grompt.py "Write a poem about AI" --model llama3-groq-8b-8192-tool-use-preview --temperature 0.8 --max_tokens 500
```

### As a Python Module

You can import and use the `rephrase_prompt` function in your Python scripts:

```python
from grompt import rephrase_prompt

original_prompt = "Write a story about a robot"
rephrased_prompt = rephrase_prompt(original_prompt)

print(rephrased_prompt)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Groq for providing the LLM services used in this utility.
- This project was inspired by the need for better prompt engineering in AI applications.