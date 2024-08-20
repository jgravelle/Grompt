import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Diagnostic information
st.write("Current working directory:", os.getcwd())
st.write("Contents of current directory:", os.listdir())
st.write("Python path:", sys.path)

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
    st.write("Added to Python path:", current_dir)

try:
    import grompt
    st.write("Successfully imported grompt")
except ImportError as e:
    st.error(f"Unable to import 'grompt': {str(e)}")
    st.stop()

try:
    from grompt import rephrase_prompt
except ImportError:
    st.error("Unable to import 'grompt'. Make sure 'grompt.py' is in the same directory as this script.")
    st.stop()

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables or use defaults
DEFAULT_MODEL = os.getenv('GROMPT_DEFAULT_MODEL', 'llama3-groq-70b-8192-tool-use-preview')
DEFAULT_TEMPERATURE = float(os.getenv('GROMPT_DEFAULT_TEMPERATURE', '0.5'))
DEFAULT_MAX_TOKENS = int(os.getenv('GROMPT_DEFAULT_MAX_TOKENS', '1024'))

# Sidebar for API key input
st.sidebar.title("Configuration")
GROQ_API_KEY = st.sidebar.text_input("Enter your GROQ API Key:", type="password")

if not GROQ_API_KEY:
    st.sidebar.warning("Please enter your GROQ API Key to use the app.")

# Main app
st.title("Grompt - Prompt Optimization Tool")

st.write("""
Grompt is a utility that uses Groq's LLM services to optimize and rephrase prompts. 
Enter your prompt below and see how Grompt can improve it!
""")

user_prompt = st.text_area("Enter your prompt:", height=100)

col1, col2, col3 = st.columns(3)
with col1:
    model = st.selectbox("Select Model", [
        "llama3-groq-70b-8192-tool-use-preview",
        "llama3-groq-8b-8192-tool-use-preview",
        "llama3-70b-8192",
        "llama3-8b-8192"
    ], index=0)
with col2:
    temperature = st.slider("Temperature", 0.0, 1.0, DEFAULT_TEMPERATURE, 0.1)
with col3:
    max_tokens = st.number_input("Max Tokens", 1, 32768, DEFAULT_MAX_TOKENS)

if st.button("Optimize Prompt"):
    if not GROQ_API_KEY:
        st.error("Please enter your GROQ API Key in the sidebar to use the app.")
    elif user_prompt:
        with st.spinner("Optimizing your prompt..."):
            # Set the API key in the environment for the rephrase_prompt function
            os.environ['GROQ_API_KEY'] = GROQ_API_KEY
            optimized_prompt = rephrase_prompt(user_prompt, model, temperature, max_tokens)
        if optimized_prompt:
            st.subheader("Optimized Prompt:")
            st.write(optimized_prompt)
    else:
        st.warning("Please enter a prompt to optimize.")

st.markdown("---")
st.write("Powered by Groq LLM services.")

# Add a note about API key security
st.sidebar.markdown("---")
st.sidebar.info(
    "Note: Your API key is used only for this session and is not stored. "
    "Always keep your API keys confidential and do not share them publicly."
)