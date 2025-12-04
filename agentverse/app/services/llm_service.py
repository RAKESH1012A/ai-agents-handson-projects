"""
LLM Service for the AgentVerse application.

This module provides functions to initialize and retrieve LLM (Large Language Model)
instances from different providers like Groq and OpenAI. It is designed to be
decoupled from the UI and other application logic.
"""

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel

def get_llm(
    provider: str, 
    api_key: str, 
    model_name: str
) -> BaseChatModel:
    """
    Initializes and returns a chat model instance based on the specified provider.

    Args:
        provider: The name of the LLM provider (e.g., "Groq", "OpenAI").
        api_key: The API key for the selected provider.
        model_name: The specific model to use.

    Returns:
        An instance of a LangChain chat model.

    Raises:
        ValueError: If the API key is missing or the provider is unsupported.
    """
    if not api_key:
        raise ValueError(f"API key for {provider} is missing.")

    if provider == "Groq":
        return ChatGroq(api_key=api_key, model=model_name)
    elif provider == "OpenAI":
        return ChatOpenAI(api_key=api_key, model=model_name)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
