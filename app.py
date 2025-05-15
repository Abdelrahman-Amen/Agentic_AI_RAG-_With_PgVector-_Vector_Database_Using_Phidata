from phi.knowledge.pdf import PDFUrlKnowledgeBase  # For creating a knowledge base from PDFs
from phi.vectordb.pgvector import PgVector, PgVector2, SearchType  # For vector database operations
from phi.agent import Agent, RunResponse  # For creating and interacting with agents
from dotenv import load_dotenv  # To load environment variables from a .env file
from phi.model.groq import Groq  # For using the Groq language model
from phi.embedder.google import GeminiEmbedder  # For embedding text with Google's Gemini Embedder
from phi.storage.agent.postgres import PgAgentStorage  # For storing agent sessions in a Postgres database
from phi.playground import Playground, serve_playground_app  # For creating a user interface for agent interaction
import os  # For environment variable management

# Load environment variables from a .env file
load_dotenv()

# Load the Groq API key from environment variables
groq_api_key = os.environ['GROQ_API_KEY']
os.environ["PHIDATA_API_KEY"] = os.getenv("PHIDATA_API_KEY")

# Define the database connection URL
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Create a knowledge base using a PDF document and a vector database
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],  # URL of the PDF document
    # Using PgVector2 for vector storage and retrieval with the Gemini embedder
    vector_db=PgVector2(collection="dish", db_url=db_url, embedder=GeminiEmbedder()),
)

# Load the knowledge base data into the database (only needed once, so can be commented out after the first run)
knowledge_base.load(upsert=True)

# Set up storage for agent sessions in a PostgreSQL database
storage = PgAgentStorage(
    table_name="agent_sessions",  # Table name for storing agent sessions
    db_url=db_url,  # Database connection URL
)

# Create an agent with the Groq model and knowledge base
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", embedder=GeminiEmbedder()),  # Groq model with Gemini embedder
    knowledge=knowledge_base,  # Attach the knowledge base to the agent
    storage=storage,  # Attach session storage
    search_knowledge=True,  # Enable knowledge base search for RAG (retrieval-augmented generation)
    show_tool_calls=True,  # Show tool calls for debugging or tracking
    markdown=True,  # Enable markdown formatting in responses
)

# Create a Playground app for user interaction with the agent
app = Playground(agents=[agent]).get_app()

# Run the app using a development server
if __name__ == "__main__":
    serve_playground_app("app:app", reload=True)

# Below code demonstrates interactive chat functionality (commented out as not part of the main functionality)

# Interactive Chat Loop
# print("Welcome to the interactive chat! Type 'exit' or 'quit' to end the conversation.")
# while True:
#     user_input = input("\nYou: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Exiting the chat. Goodbye!")
#         break

#     # Generate response
#     response = agent.run(user_input)
#     print("\nAssistant:", response.content if isinstance(response, RunResponse) else response)













# Another code with same Strategy




# import typer
# from typing import Optional,List
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.assistant import Assistant
# from phi.storage.agent.postgres import PgAgentStorage
# from phi.knowledge.pdf import PDFUrlKnowledgeBase
# from phi.vectordb.pgvector import PgVector2
# from phi.embedder.google import GeminiEmbedder

# import os
# from dotenv import load_dotenv
# load_dotenv()


# os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# # Ensure that API keys are set properly
# if not os.environ["GROQ_API_KEY"] or not os.environ["GOOGLE_API_KEY"]:
#     raise ValueError("Missing API Keys! Check your .env file.")

# db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# knowledge_base=PDFUrlKnowledgeBase(
#     urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
#     vector_db=PgVector2(collection="dish",db_url=db_url,embedder=GeminiEmbedder()),
#     chunk=False
# )

# knowledge_base.load()

# storage = PgAgentStorage(
#     table_name="pdf_assistant",
#     db_url=db_url,
# )
# def pdf_assistant(new: bool = False, user: str = "user"):
#     run_id: Optional[str] = None

#     assistant = Agent(
#         model=Groq(id="llama-3.3-70b-versatile", embedder=GeminiEmbedder()),
#         run_id=run_id,
#         user_id=user,
#         knowledge_base=knowledge_base,
#         storage=storage,
#         show_tool_calls=True,
#         search_knowledge=True,
#         read_chat_history=True,
#     )

#     if run_id is None:
#         run_id = assistant.run_id
#         print(f"Started Run: {run_id}\n")
#     else:
#         print(f"Continuing Run: {run_id}\n")

#     assistant.cli_app(markdown=True)

# if __name__ == "__main__":
#     typer.run(pdf_assistant)