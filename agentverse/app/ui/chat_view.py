"""
Defines the main chat view UI component for the AgentVerse Streamlit application.
"""

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

def render(graph, user_message: str, use_case: str):
    """
    Renders the chat interaction for a given user message and agent graph.

    This function displays the user's message, streams the agent's response,
    and updates the session state with the conversation history.

    Args:
        graph: The compiled LangGraph agent to execute.
        user_message: The message input by the user.
        use_case: The name of the currently selected agent use case.
    """
    # Add user message to chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    st.session_state.messages.append(HumanMessage(content=user_message))

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Stream agent response
    with st.chat_message("assistant"):
        # The placeholder will be updated with the streaming response
        response_placeholder = st.empty()
        full_response = ""

        # The input to the graph is a dictionary matching the AgentState structure
        inputs = {"messages": [HumanMessage(content=user_message)]}

        if use_case == "Basic Chatbot":
            for event in graph.stream(inputs, stream_mode="values"):
                # The event is the entire state, we access the last message
                message = event["messages"][-1]
                if isinstance(message, AIMessage):
                    full_response += message.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append(AIMessage(content=full_response))
        # Add other use cases here with an 'elif'
        else:
            st.error(f"Chat rendering not implemented for use case: {use_case}")
