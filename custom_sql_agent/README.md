Custom SQL Agent with LangGraph and Azure OpenAI

  This project demonstrates an advanced, stateful SQL agent built with LangChain, LangGraph, and Azure OpenAI. The agent is capable of understanding a database's structure and answering natural language
  questions by generating, validating, and executing SQL queries against it.

  ✨ Features

   - Natural Language to SQL: Ask complex questions in plain English and receive precise answers from your database.
   - Stateful Reasoning: Utilizes LangGraph to create a robust, multi-step process for database interaction, including schema discovery, query generation, and self-correction.
   - Powered by Azure OpenAI: Leverages the power of Azure OpenAI's GPT models for intelligent query generation and response formulation.
   - Comprehensive DB Toolkit: The agent is equipped with a full suite of tools to list tables, inspect schemas, check query syntax, and execute queries.
   - Classic Sample Database: Comes pre-configured to work with the standard Chinook SQLite database, which is downloaded automatically.

  🏛️ How It Works: The Agent's Workflow

  The agent follows a sophisticated, graph-based workflow to ensure accuracy and efficiency:

   1. List Tables: The agent first identifies all available tables in the database to understand the overall scope.
   2. Get Schema: Based on the user's question, it inspects the schema of the most relevant tables to understand their columns and relationships.
   3. Generate Query: With a clear understanding of the schema, it constructs a syntactically correct SQL query to answer the question.
   4. Check Query: Before execution, the agent validates the query for common mistakes and correctness, refining it if necessary.
   5. Run Query: The validated query is executed against the database.
   6. Formulate Answer: The agent analyzes the query results and provides a final, easy-to-understand answer in natural language.

  🚀 Getting Started

  Follow these steps to set up and run the SQL agent on your local machine.

  1. Prerequisites

   - Python 3.13.9
   - An active Azure OpenAI account with a deployed GPT model (e.g., gpt-4o).

  2. Setup & Installation

   1. Clone the Repository:

   1     git clone https://github.com/RAKESH1012A/ai-agents-handson-projects.git
   2     cd custom_sql_agent

   2. Create and Activate a Virtual Environment:

   1     # Create a virtual environment
   2     python -m venv venv
   3 
   4     # Activate the environment
   5     # On Windows:
   6     venv\Scripts\activate
   7     # On macOS/Linux:
   8     source venv/bin/activate

   3. Install Dependencies:
      Create a requirements.txt file with the following content:

   1     python-dotenv
   2     openai
   3     langchain
   4     langchain-community
   5     langchain-openai
   6     requests
      Then, install the dependencies:
   1     pip install -r requirements.txt

   4. Configure Environment Variables:
       - Create a new file named .env in the custom_sql_agent directory by copying the .env.example file.
       - Open the .env file and add your specific Azure OpenAI credentials:

   1         AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
   2         AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"
   3         OPENAI_API_VERSION="your-api-version" # e.g., 2024-02-01
   4         AZURE_OPENAI_DEPLOYMENT_NAME="your-deployment-name"

  3. Usage

  This project is delivered as a Jupyter Notebook (agent.ipynb).

   1. Open the Notebook: Launch agent.ipynb in a compatible environment like VS Code, Jupyter Lab, or Google Colab.
   2. Run the Cells: Execute the cells in the notebook sequentially. The notebook will handle:
       - Installing any necessary packages (if you skipped step 3).
       - Loading your environment variables.
       - Downloading the Chinook.db sample database.
       - Building and compiling the agent graph.
       - Running a sample query.

  demo-gif.gif

  Example Interaction

  The final cell in the notebook demonstrates the agent's capabilities with a sample question.

  User Question:
  > "Which genre on average has the longest tracks?"

  Agent's Final Answer:
  > The genre with the longest average track length is "Sci Fi & Fantasy," followed by:
  >
  > 1.  Sci Fi & Fantasy: 2,911,783 milliseconds
  > 2.  Science Fiction: 2,625,549 milliseconds
  > 3.  Drama: 2,575,283 milliseconds
  > 4.  TV Shows: 2,145,041 milliseconds
  > 5.  Comedy: 1,585,263 milliseconds

  You can modify the question variable in the last cell to ask your own questions and explore the database.