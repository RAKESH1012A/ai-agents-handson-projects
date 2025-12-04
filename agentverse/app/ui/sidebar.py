"""
Defines the sidebar UI component for the AgentVerse Streamlit application.
"""

import streamlit as st
from config.app_config import app_config
from typing import Dict, Any

def render() -> Dict[str, Any]:
    """
    Renders the sidebar UI using Streamlit and returns the user's selections.

    This function populates the sidebar with options for LLM providers, models,
    and use cases based on the application configuration. It also handles the
    logic for API key input.

    Returns:
        A dictionary containing the user's selected controls and inputs.
    """
    user_controls = {}
    st.set_page_config(
        page_title=f"🤖 {app_config.get_page_title()}",
        layout="wide"
    )
    st.header(f"🤖 {app_config.get_page_title()}")

    with st.sidebar:
        st.subheader("🛠️ Configuration")

        # LLM provider selection
        llm_providers = app_config.get_llm_providers()
        selected_provider = st.selectbox("Select LLM Provider", llm_providers)
        user_controls["selected_provider"] = selected_provider

        # Model and API key selection based on provider
        if selected_provider == 'Groq':
            groq_models = app_config.get_groq_models()
            user_controls["selected_model"] = st.selectbox("Select Model", groq_models)
            
            # Use session state to persist the API key across reruns
            if "GROQ_API_KEY" not in st.session_state:
                st.session_state["GROQ_API_KEY"] = ""
            
            user_controls["api_key"] = st.text_input(
                "Groq API Key", 
                type="password", 
                key="GROQ_API_KEY"
            )
            
            if not user_controls["api_key"]:
                st.warning("Please enter your Groq API key.")

        elif selected_provider == 'OpenAI':
            openai_models = app_config.get_openai_models()
            user_controls["selected_model"] = st.selectbox("Select Model", openai_models)
            
            if "OPENAI_API_KEY" not in st.session_state:
                st.session_state["OPENAI_API_KEY"] = ""

            user_controls["api_key"] = st.text_input(
                "OpenAI API Key", 
                type="password", 
                key="OPENAI_API_KEY"
            )
            if not user_controls["api_key"]:
                st.warning("Please enter your OpenAI API key.")

        st.divider()
        
        # Use case selection
        use_cases = app_config.get_use_cases()
        user_controls["selected_use_case"] = st.selectbox("Select Agent Usecase", use_cases)

    return user_controls
