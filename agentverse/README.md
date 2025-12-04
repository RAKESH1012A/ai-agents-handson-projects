# AgentVerse: A Multi-Agent Chatbot Platform

AgentVerse is a production-ready, scalable framework for building and serving stateful, agentic AI chatbots using LangGraph and Streamlit. It provides a clean architecture that allows for the easy addition of new, independent agents, each with their own unique tools and logic.

## ✨ Features

- **Scalable Architecture**: A modular structure that separates UI, configuration, services, and agent logic, allowing for independent development and scaling.
- **Multi-Agent Ready**: Easily extend the platform by adding new agent definitions in the `app/agents` directory.
- **Powered by LangGraph**: Leverages LangGraph to build robust, stateful agents capable of complex, multi-step reasoning.
- **Interactive UI**: Built with Streamlit for a user-friendly, real-time chat experience.
- **Flexible LLM Configuration**: Easily configure different LLMs and models (starting with Groq).

## 🏛️ Architecture Overview

The project is structured for clarity and scalability:

-   `agentverse/`: The root of the project.
    -   `main.py`: The main application entry point.
    -   `app/`: Contains the core application logic.
        -   `main.py`: The primary Streamlit application orchestrator.
        -   `agents/`: Each file here defines a self-contained agent graph (e.g., `basic_chatbot.py`).
        -   `services/`: Houses business logic, such as the `llm_service` for initializing LLMs.
        -   `ui/`: Contains all Streamlit UI components (e.g., `sidebar.py`, `chat_view.py`).
    -   `config/`: Manages application configuration.
        -   `settings.ini`: A static configuration file for UI options, models, etc.
        -   `app_config.py`: A service to load and parse `settings.ini`.
    -   `requirements.txt`: Project dependencies.
    -   `.env`: For storing secrets like API keys (create this from `.env.example`).
    -   `.gitignore`: Specifies files and directories to be ignored by version control.

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### 1. Prerequisites

-   Python 3.13.9
-   A Groq API Key

### 2. Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd agentverse
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your API key:**
    -   Create a new file named `.env` in the root of the project.
    -   Add your Groq API key to the file:
        ```
        GROQ_API_KEY="your-groq-api-key-here"
        ```

### 3. Running the Application

Launch the Streamlit application with the following command:

```bash
streamlit run main.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 🛠️ How to Add a New Agent

The `AgentVerse` architecture makes it simple to add new agents:

1.  **Define the Agent Logic:**
    -   Create a new Python file in the `app/agents/` directory (e.g., `my_new_agent.py`).
    -   Inside this file, create a function `create_my_new_agent_graph(llm)` that builds and returns a compiled LangGraph graph. You can define new nodes and states as needed.

2.  **Update the Configuration:**
    -   Add the name of your new agent (e.g., "My New Agent") to the `USECASE_OPTIONS` in `config/settings.ini`.

3.  **Integrate into the UI:**
    -   In `app/main.py`, add a case in the `get_graph_for_usecase` function to call your new `create_my_new_agent_graph` function when your use case is selected.

That's it! Your new agent will now be available for selection in the Streamlit UI.
