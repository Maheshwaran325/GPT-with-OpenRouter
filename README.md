# GPT with OpenRouter

## Overview

 GPT is an interactive web application that enables users to engage in conversations with various language models (LLMs) provided by OpenRouter. Users can choose from a range of LLMs and interact with them in a natural language format, experiencing the capabilities of these advanced AI systems. 

## Features

- Integration with OpenRouter API for access to multiple language models
- Dynamic model selection with information tooltips
- Adjustable AI parameters (temperature and max tokens)
- File upload functionality for text documents
- User-friendly interface built with Streamlit

## Prerequisites

- Python 3.7+
- OpenRouter API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Maheshwaran325/GPT-with-OpenRouter.git
   cd streamlit-gpt
   ```

2. Create a virtual environment 
    ```
    python -m venv .venv
    .venv\scripts\activate  # for windows
    ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenRouter API key:
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your API key to the file:
     ```
     OPENROUTER_API_TOKEN = "your-api-key-here"
     ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run Chatbot.py
   ```

2. Open your web browser and go to `http://localhost:8501`

3. Upload a text file using the file uploader

4. Select a language model and adjust the AI parameters if desired

5. Ask a question about the uploaded article in the text input field

6. View the AI-generated response

## Project Structure

- `app.py`: Main application file
- `components/Sidebar.py`: Sidebar component for model selection and parameters
- `shared/constants.py`: Constant values used across the application
- `requirements.txt`: List of Python dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the wonderful web application framework
- [OpenRouter](https://openrouter.ai/) for providing access to various language models
