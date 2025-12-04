"""
AgentVerse Application Entry Point

This script serves as the main entry point for running the AgentVerse
Streamlit application. It imports and executes the primary app logic.
"""

from app.main import main
import streamlit as st
import os

# Set custom Streamlit theme
# This will be automatically picked up by Streamlit when the app runs.
# We create the .streamlit directory and config.toml file if they don't exist.
def apply_theme():
    streamlit_dir = ".streamlit"
    config_path = os.path.join(streamlit_dir, "config.toml")
    
    if not os.path.exists(config_path):
        os.makedirs(streamlit_dir, exist_ok=True)
        theme_config = """
                        [theme]
                        primaryColor="#00A67E"
                        backgroundColor="#FFFFFF"
                        secondaryBackgroundColor="#F0F2F6"
                        textColor="#262730"
                        font="sans serif"
                        """
        with open(config_path, "w") as f:
            f.write(theme_config)

if __name__ == "__main__":
    # Ensure a .env file exists for API key management
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write('GROQ_API_KEY=""')
            f.write('OPENAI_API_KEY=""')

    apply_theme()
    main()

