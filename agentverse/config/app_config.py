"""
Configuration service for the AgentVerse application.

This module provides a singleton class `AppConfig` to load and parse
the `settings.ini` file, offering a clean and typed interface to access
application settings.
"""

from configparser import ConfigParser
from typing import List
import os

class AppConfig:
    """A service to load and provide access to application settings."""

    def __init__(self, config_file: str = "config/settings.ini"):
        """
        Initializes the configuration service.

        Args:
            config_file: The path to the configuration file.
        """
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file not found: {config_file}")
        
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self) -> str:
        """Returns the page title for the Streamlit UI."""
        return self.config.get("ui", "PAGE_TITLE", fallback="AgentVerse")

    def get_llm_providers(self) -> List[str]:
        """Returns the list of supported LLM providers."""
        providers = self.config.get("llm", "PROVIDERS", fallback="Groq")
        return [provider.strip() for provider in providers.split(",")]

    def get_groq_models(self) -> List[str]:
        """Returns the list of available Groq models."""
        models = self.config.get("llm", "GROQ_MODELS", fallback="llama-3.1-8b-instant")
        return [model.strip() for model in models.split(",")]
    
    def get_openai_models(self) -> List[str]:
        """Returns the list of available OpenAI models."""
        models = self.config.get("llm", "OPENAI_MODELS", fallback="gpt-4o")
        return [model.strip() for model in models.split(",")]

    def get_use_cases(self) -> List[str]:
        """Returns the list of available agent use cases."""
        use_cases = self.config.get("agent", "USECASES", fallback="Basic Chatbot")
        return [use_case.strip() for use_case in use_cases.split(",")]

# Create a singleton instance to be used throughout the application
app_config = AppConfig()
