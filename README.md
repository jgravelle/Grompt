# Grompt Utility

Grompt is a Python utility that uses the Groq LLM provider service to instantly refactor amazingly detailed and effective prompts. It's designed to optimize user prompts for better results when working with large language models.

![image](https://github.com/user-attachments/assets/1bac9737-57e9-4970-aa3a-5f1c078ca2d9)

## Features

- Rephrase and optimize user prompts using Groq's LLM services
- Configurable via environment variables or .env file
- Can be used as a module in other Python scripts or run from the command line
- Supports various Groq models and customizable parameters
- Includes a separate Streamlit web app for easy demonstration and testing
- Streamlit app supports API key input for use in hosted environments

## Prerequisites

- Python 3.6 or higher
- A Groq API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/jgravelle/Grompt.git
   cd Grompt
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Adding Grompt to Your Project

To use Grompt in your project, you only need to include the `Grompt.py` file. Follow these steps:

1. Copy the `Grompt.py` file into your project directory.
2. Install the required dependencies:
   ```
   pip install groq python-dotenv
   ```
3. Import and use the `rephrase_prompt` function in your Python scripts:
   ```python
   from Grompt import rephrase_prompt

   original_prompt = "Write a story about a robot"
   rephrased_prompt = rephrase_prompt(original_prompt)

   print(rephrased_prompt)
   ```

## File Structure

- `Grompt.py`: The main Grompt utility file
- `streamlit_app.py`: A separate Streamlit app for demonstrating Grompt's capabilities
- `.env`: Configuration file for environment variables
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

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

### Streamlit Web App

To run the Streamlit web app for an interactive demo:

```
streamlit run streamlit_app.py
```

This will start a local web server and open the Grompt demo in your default web browser. You can enter prompts, adjust parameters, and see the optimized results in real-time.

When using the Streamlit app in a hosted environment:

1. Look for the sidebar on the left side of the app.
2. Enter your Groq API key in the "Enter your GROQ API Key:" field.
3. Your API key will be used only for the current session and is not stored.

Note: Always keep your API keys confidential and do not share them publicly.

### As a Command-Line Tool

Run Grompt from the command line:

```
python Grompt.py "Your prompt here" [--model MODEL] [--temperature TEMP] [--max_tokens MAX_TOKENS]
```

Options:
- `--model`: Specify the Groq model to use (overrides the default)
- `--temperature`: Set the temperature for text generation (overrides the default)
- `--max_tokens`: Set the maximum number of tokens to generate (overrides the default)

Example:
```
python Grompt.py "Write a poem about AI" --model llama3-groq-8b-8192-tool-use-preview --temperature 0.8 --max_tokens 500
```

### Practical Example

Here's an example of Grompt in action:

```
C:\ai\Grompt> python Grompt.py "Write an 11th grade level report on quantum physics"
Rephrased prompt:
"Compose a comprehensive report on quantum physics, tailored to an 11th-grade reading level, that includes clear explanations of key concepts, historical background, and real-world applications. Ensure the report is engaging, informative, and easy to understand for students at this level. Include relevant examples and diagrams to illustrate complex ideas. The report should be well-structured, with logical flow between sections, and should not exceed 2000 words. Please adhere to academic writing standards and provide a list of credible sources used in the research."
```

This example demonstrates how Grompt takes a simple, open-ended prompt and transforms it into a detailed, structured prompt that is likely to produce a high-quality response from an LLM.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Include the name 'J. Gravelle' somewhere in your code and docs if you use this. He's full of himself.

## Acknowledgments

- Thanks to Groq for providing the LLM services used in this utility.
- This project was inspired by the need for better prompt engineering in AI applications.
- Created by J. Gravelle, who is indeed full of himself.
