#  Building Agentic AI RAG With (PgVector) Vector Database Using Phidata ⚡🚀

This project showcases how to extract information from a PDF document, query it using natural language, and retrieve accurate responses. The application leverages **PgVector** for vector storage, **Groq API** for advanced language modeling, and **PhiData API** for embedding and agent knowledge handling.

![Image](https://github.com/user-attachments/assets/ce378a8f-bac0-419c-a3c9-aac9a094a371)

## 🌟 Key Features

- **PDF Knowledge Base**: Convert PDF documents into searchable knowledge bases.
- **PgVector Database**: Store vector embeddings for efficient retrieval.
- **Groq Language Model**: Advanced text generation and question-answering capabilities.
- **Playground UI**: Interactive web-based GUI for user-agent interaction.
- **Two Implementations**: Flexible CLI-based assistant and a Playground GUI.

---

## 🛠️ Requirements

Before running the application, ensure you have the following installed:

- **Docker**
- **Python**
- **PgVector Database**
- **API Keys for Groq and PhiData**

---

## 🐳 Setting Up the PgVector Database

To initialize the PgVector database, run the following **Docker** command:

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16

```
This command creates a PostgreSQL database with vector capabilities and configures it for our application.

---

## ⚙️ Setting Up Environment Variables

Create a `.env` file in your project directory with the following keys:

```env
GROQ_API_KEY=your_groq_api_key
PHIDATA_API_KEY=your_phidata_api_key

```

Make sure the API keys are valid and correctly configured.

---

## 🚀 Running the Playground GUI

### Code Overview

The Playground interface enables users to interact with the agent in a user-friendly GUI. Here’s what happens:

1. **Knowledge Base Creation**:
   - Extracts data from a PDF (`ThaiRecipes.pdf` in this example).
   - Embeds data using the **GeminiEmbedder** from PhiData.
   - Stores embeddings in **PgVector2**.

2. **Agent Integration**:
   - Uses the **Groq Model** (`llama-3.3-70b-versatile`) for advanced language understanding.
   - Connects the agent to the knowledge base for **retrieval-augmented generation (RAG)**.

3. **User Interaction**:
   - Runs app with an interactive Playground UI.
   - Users can query the knowledge base, and the agent responds in real-time.

### Run the App

```bash
python app.py
```

This will start a development server. Open the browser at the displayed URL to access the Playground.

---


---

## 🌐 APIs Used

1. **Groq API**:
   - Powers the language model for natural language processing.
   - Provides advanced text generation and understanding capabilities.

2. **PhiData API**:
   - Handles embeddings and agent knowledge.
   - Integrates seamlessly with PgVector for vector storage.

---

## 🗂️ Folder Structure

```
project/
├── app.py                   # Playground GUI code
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── Dockerfile               # Docker configuration for the app
```

---

## ✨ How It Works

1. **PDF to Knowledge Base**:
   - Extracts content from the PDF.
   - Splits content into chunks and embeds them.

2. **Knowledge Search**:
   - Queries are embedded and compared with stored vectors using PgVector.
   - The best-matching chunk is retrieved for answering queries.

3. **Agent Response**:
   - Uses Groq API to generate responses based on retrieved knowledge.
   - Outputs responses in markdown format (GUI).

---


# Demo 📽

Below is a demonstration of how the application works:

![Demo of the Application](https://github.com/Abdelrahman-Amen/Agentic_AI_RAG-_With_PgVector-_Vector_Database_Using_Phidata/blob/main/Demo.gif)
