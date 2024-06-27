import streamlit as st
import requests
import json
from shared import constants, utils

def get_available_models():
    try:
        response = requests.get(constants.OPENROUTER_API_BASE + "/models")
        response.raise_for_status()
        models = json.loads(response.text)["data"]
        return [(model["id"], model.get("pricing", {}).get("prompt") == "0", model) for model in models]
    except requests.exceptions.RequestException as e:
        st.error(f"Error getting models from API: {e}")
        return []

def handle_model_selection(available_models, selected_model, default_model):
    model_names = [f"{model[0]} 🎁" if model[1] else model[0] for model in available_models]
    
    selected_index = None
    if selected_model:
        selected_index = next((i for i, m in enumerate(available_models) if m[0] == selected_model), None)
    if selected_index is None:
        selected_index = next((i for i, m in enumerate(available_models) if m[0] == default_model), 0)

    selected_model_name = st.selectbox(
        "Select a model", model_names, index=selected_index
    )
    
    selected_model_info = next(model for model in available_models if model[0] == selected_model_name.replace(" 🎁", ""))
    
    st.markdown("**Model Info**")
    st.markdown(f"**Context:** {selected_model_info[2].get('context_length')}")
    st.markdown(f"**Architecture:** {selected_model_info[2].get('architecture')}")
    
    return selected_model_name.replace(" 🎁", "")

def sidebar(default_model):
    with st.sidebar:
        st.title('🦙💬 Llama 2 Chatbot')
        if 'OPENROUTER_API_TOKEN' in st.secrets:
            st.success('API key already provided!', icon='✅')
            api_key = st.secrets['OPENROUTER_API_TOKEN']
        else:
            api_key = st.text_input('Enter OpenRouter API token:', type='password')
            if not api_key:
                st.warning('Please enter your credentials!', icon='⚠️')
            else:
                st.success('Proceed to entering your prompt message!', icon='👉')

        available_models = get_available_models()
        selected_model = handle_model_selection(available_models, st.session_state.get("model"), default_model)
        st.query_params["model"] = selected_model
        st.session_state["model"] = selected_model

        st.subheader("Model Parameters")
        temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1,
                                help="Higher values make the output more random, lower values make it more deterministic.")
        max_tokens = st.slider("Max Tokens", min_value=50, max_value=4000, value=1000, step=50,
                               help="The maximum number of tokens to generate in the chat completion.")

    return api_key, selected_model, temperature, max_tokens

# The exchange_code_for_api_key function remains unchanged