"""
Defines the Basic Chatbot agent for the AgentVerse application.

This module contains the node logic for the chatbot's processing step
and the graph construction function to build the corresponding LangGraph agent.
"""

from langgraph.graph import StateGraph, START, END
from app.agents.state import AgentState
from langchain_core.language_models.chat_models import BaseChatModel

# --- 1. Node Definition ---

class BasicChatbotNode:
    """
    A simple node that invokes the LLM with the current state and returns the response.
    """
    def __init__(self, llm: BaseChatModel):
        """
        Initializes the node with a language model.

        Args:
            llm: An instance of a LangChain chat model.
        """
        self.llm = llm

    def process(self, state: AgentState) -> dict:
        """
        Processes the input state, invokes the LLM, and returns the updated state.
        
        Args:
            state: The current state of the graph.

        Returns:
            A dictionary with the updated messages.
        """
        response = self.llm.invoke(state['messages'])
        return {"messages": [response]}

# --- 2. Graph Construction ---

def create_basic_chatbot_graph(llm: BaseChatModel):
    """
    Builds and compiles the graph for a basic, single-node chatbot.

    Args:
        llm: An instance of a LangChain chat model to be used by the node.

    Returns:
        A compiled LangGraph instance.
    """
    graph_builder = StateGraph(AgentState)
    
    # Initialize the node
    basic_chatbot_node = BasicChatbotNode(llm)
    
    # Add the node and define the graph's flow
    graph_builder.add_node("chatbot", basic_chatbot_node.process)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    
    return graph_builder.compile()
