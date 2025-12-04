"""
Main application orchestrator for the AgentVerse Streamlit app.

This script ties together the UI components, configuration, services, and agent
graphs to create a functional, multi-agent chatbot platform.
"""

import streamlit as st
from app.ui import sidebar, chat_view
from app.services import llm_service
from app.agents import basic_chatbot
from dotenv import load_dotenv

def get_graph_for_use_case(use_case: str, llm):
    """
    Acts as a factory to retrieve the correct agent graph based on the
    selected use case.

    Args:
        use_case: The name of the selected use case.
        llm: The initialized language model instance.

    Returns:
        A compiled LangGraph instance for the selected agent.
    """
    if use_case == "Basic Chatbot":
        return basic_chatbot.create_basic_chatbot_graph(llm)
    # To add a new agent, add an 'elif' condition here
    # elif use_case == "My New Agent":
    #     return my_new_agent.create_my_new_agent_graph(llm)
    else:
        return None

def main():
    """
    The main function that orchestrates the Streamlit application.
    """
    # Load environment variables for API keys
    load_dotenv()
    
    # 1. Render the sidebar and get user-selected configurations
    user_controls = sidebar.render()

    # 2. Initialize the LLM based on user selections
    # We use a placeholder for the graph until the LLM is ready
    graph = None
    try:
        provider = user_controls.get("selected_provider")
        model_name = user_controls.get("selected_model")
        api_key = user_controls.get("api_key")
        
        # Only proceed if the necessary components are available
        if provider and model_name and api_key:
            llm = llm_service.get_llm(
                provider=provider,
                api_key=api_key,
                model_name=model_name
            )
            
            # 3. Get the appropriate agent graph for the selected use case
            use_case = user_controls.get("selected_use_case")
            graph = get_graph_for_use_case(use_case, llm)
        
    except ValueError as e:
        st.error(f"Failed to initialize LLM: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

    # 4. Handle the chat interaction
    # Display previous messages from session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message.type):
            st.markdown(message.content)

    # Get new user input
    user_message = st.chat_input("Enter your message...")

    if user_message:
        if not graph:
            st.warning("Please ensure your API key is entered and all options are selected.")
        else:
            # Render the chat response
            chat_view.render(
                graph=graph, 
                user_message=user_message,
                use_case=user_controls.get("selected_use_case")
            )
