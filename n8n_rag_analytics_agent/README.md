n8n RAG Chatbot with Automated Analytics

  This project is an advanced, automated RAG (Retrieval-Augmented Generation) system built entirely on the n8n low-code platform. It provides a complete, end-to-end solution for creating a knowledge    
  base from documents, answering questions via a chatbot, and monitoring its own performance through automated daily analytics.

  ✨ Key Features

   - Form-Based Document Upload: Easily build a knowledge base by uploading PDF, CSV, or JSON files through a simple web form.
   - RAG Chatbot: A conversational AI agent that answers user questions based only on the content of the uploaded documents, preventing hallucinations.
   - Vector Search Integration: Uses Pinecone to store document embeddings and retrieve relevant context for answering questions.
   - Automated Daily Analytics: A scheduled workflow runs daily to analyze all chat interactions and calculate key performance metrics (e.g., total questions, success rate, failed lookups).
   - Email Reporting: Automatically sends a daily performance summary report via Gmail, providing clear insights into the chatbot's usage and effectiveness.
   - Multi-LLM Ready: Configured to use fast and efficient LLMs like Groq for chat responses, while leveraging OpenAI for high-quality embeddings.
   - Low-Code Implementation: The entire system is orchestrated using n8n's visual workflow builder, making it easy to understand, modify, and extend.

  🏛️ Workflow Architecture

  The agent.json file contains three distinct, interconnected workflows that work together to provide the full functionality.

  Workflow 1: Document Ingestion
   - Trigger: An n8n Form that allows users to upload one or more documents.
   - Process:
       1. The uploaded file's text content is extracted.
       2. The text is processed, chunked, and converted into vector embeddings using OpenAI.
       3. The embeddings and content are stored in a specified Pinecone index.
       4. Submission metadata is logged to a persistent n8n Data Table.

  Workflow 2: RAG Chat
   - Trigger: An n8n Chat Trigger that provides a shareable web interface for conversation.
   - Process:
       1. A user's question is received by a LangChain Agent node.
       2. The agent uses a Pinecone Retriever Tool to search the vector store for documents relevant to the user's question.
       3. The retrieved context and the original question are passed to a Groq LLM (e.g., Llama 3).
       4. The LLM generates an answer based only on the provided context.
       5. The conversation history is maintained for contextual follow-up questions.
       6. The final interaction is logged to an n8n Data Table.

  Workflow 3: Daily Analytics
   - Trigger: An n8n Schedule Trigger configured to run every day at a set time (e.g., 9 AM).
   - Process:
       1. The workflow fetches all chat logs from the past 24 hours from the n8n Data Table.
       2. A Code node runs JavaScript to analyze the logs, calculating total questions, success rates (based on whether the agent could find an answer), and the most referenced documents.
       3. The results are formatted into an HTML report.
       4. The report is sent to a specified email address using the Gmail node.

  🚀 Setup and Installation

  To use this workflow, you need an n8n instance and accounts for the integrated services.

  1. Prerequisites

   - An n8n instance (either Cloud or self-hosted).
   - A Pinecone account (you will need your API key).
   - An OpenAI API key (for generating embeddings).
   - A Groq API key (for the chat LLM).
   - A Gmail account, with OAuth set up in n8n to allow sending emails.

  2. How to Import and Configure

   1. Import the Workflow:
       - Open your n8n canvas.
       - Click File > Import from file....
       - Select the agent.json file from this project.
       - The entire workflow, including all three trigger points, will be imported onto your canvas.

   2. Configure Credentials:
       - In your n8n instance, navigate to the Credentials section from the left-hand menu.
       - Click Add credential and create new credentials for each of the following services, pasting in your API keys where required:
           - Pinecone
           - OpenAI
           - Groq
           - Gmail (this will require an OAuth authentication flow).

   3. Connect Nodes to Credentials:
       - Find the following nodes in the workflow and use the dropdown menus to select the credentials you just created:
           - OpenAI Embeddings (Select your OpenAI credential).
           - Pinecone Insert Documents (Select your Pinecone credential).
           - Pinecone Retrieve Tool (Select your Pinecone credential).
           - Groq Chat Model (Select your Groq credential).
           - Send Daily Summary Email (Select your Gmail credential).

   4. Customize Node Parameters:
       - In the Pinecone nodes, specify the name of your Pinecone index.
       - In the Send Daily Summary Email node, change the recipient email address to your own.

   5. Activate the Workflow:
       - Click the "Active" toggle at the top of the screen. This will activate all three triggers, making the form and chat UIs public and enabling the daily schedule.

  ⚙️ How to Use

   - Uploading Documents: Find the "Document Upload Form" node, click the URL in its parameter view, and use the web form to upload your knowledge base files.
   - Chatting with the Agent: Find the "Chat Trigger" node and open its URL to start a conversation with your RAG agent.
   - Receiving Analytics: The analytics email will be sent automatically every day to the email address you configured.

  Example Daily Analytics Email

  Subject: Daily RAG Chatbot Summary - 2024-12-04

  > ## Daily RAG Chatbot Summary
  >
  > Period: Last 24 hours
  >
  > Total Questions Asked: 42
  >
  > Success Rate: 90.5%
  >
  > Failed Lookups: 4
  >
  > ### Top Referenced Files
  >
  > -   project_specs.pdf: 15 references
  > -   onboarding_guide.pdf: 10 references
  > -   q3_financials.csv: 8 references
  >
  > Generated automatically by n8n RAG Chatbot