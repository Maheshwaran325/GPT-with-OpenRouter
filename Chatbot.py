import streamlit as st
from openai import OpenAI
from components.Sidebar import sidebar
from shared import constants

# Call the sidebar function to get API key, selected model, temperature, and max_tokens
api_key, selected_model, temperature, max_tokens = sidebar(constants.OPENROUTER_DEFAULT_CHAT_MODEL)

st.title("💬 Streamlit GPT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What is your question?"):
    if not api_key:
        st.info("Please add your OpenRouter API key to continue.")
        st.stop()

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Create OpenAI client with OpenRouter base URL
    client = OpenAI(api_key=api_key, base_url=constants.OPENROUTER_API_BASE)

    # Get assistant response
    response = client.chat.completions.create(
        model=selected_model,
        messages=st.session_state.messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    assistant_message = response.choices[0].message.content

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_message)

# Clear chat button (you can move this to the sidebar file if preferred)
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]
    st.experimental_rerun()