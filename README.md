# Streamlit GPT: File Q&A with OpenRouter

## Overview

Streamlit GPT is an interactive web application that allows users to upload text files and ask questions about their content using various language models provided by OpenRouter. The application leverages the power of advanced language models to analyze uploaded articles and provide intelligent responses to user queries.

## Features

- File upload functionality for text documents
- Integration with OpenRouter API for access to multiple language models
- Dynamic model selection with information tooltips
- Adjustable AI parameters (temperature and max tokens)
- User-friendly interface built with Streamlit

## Prerequisites

- Python 3.7+
- OpenRouter API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/streamlit-gpt.git
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the wonderful web application framework
- [OpenRouter](https://openrouter.ai/) for providing access to various language models#   G P T - w i t h - O p e n R o u t e r  
 #   G P T - w i t h - O p e n R o u t e r  
 