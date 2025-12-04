"""
Defines the shared state for all agent graphs in the AgentVerse application.
"""

from typing import List, Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """
    Represents the structure of the state used in all agent graphs.

    Attributes:
        messages: A list of messages, annotated to be managed by `add_messages`
                  which appends new messages to the list.
    """
    messages: Annotated[List, add_messages]
