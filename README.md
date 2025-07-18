

# Pathology-RAG-Mistral

A local Retrieval-Augmented Generation (RAG) system for **pathology** documents, powered by **vector databases (ChromaDB)** and processed with the **Mistral language model** through Ollama. This project enables efficient search and natural language question-answering over large collections of digital documents.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Terminology](#key-terminology)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)


## Project Overview

**Pathology-RAG-Mistral** leverages modern NLP techniques to let users ask questions about pathology documents. It splits documents, generates vector embeddings for efficient search, and uses a local Mistral LLM (via Ollama) to produce relevant answers based on retrieved context. Everything runs locally, ensuring privacy and control over sensitive medical data.

## Key Terminology

### Retrieval-Augmented Generation (RAG)

- A hybrid system that first **retrieves relevant information** from a database and then **generates answers** using a language model, improving accuracy and grounding responses in your actual data.


### ChromaDB (Vector Database)

- **ChromaDB** is a lightweight, fast, and local **vector database**. It stores document chunks as high-dimensional vectors, enabling efficient similarity search.


### Ollama

- A tool for running large language models (like **Mistral**) **locally** on your machine, without the need for cloud APIs or internet access.


### Embedding Function

- Transforms text (e.g., document chunks and queries) into **vector representations**. Similar content creates similar vectors, forming the core of the search process.


### Vector Database

- A database designed for storing and searching by **vector embeddings** instead of traditional structured data. Useful for semantic search in NLP.


## Requirements

- Python 3.10 or newer
- `pip` (Python package manager)
- Pathology PDFs in a `data` directory for ingestion
- [Ollama](https://ollama.com/) installed and running with the **Mistral** model downloaded locally


### Python Packages

- `chromadb`
- `langchain`
- `langchain-community`
- `langchain-chroma`
- `langchain_ollama`
- `fastembed` (for fast local embeddings)
- `PyPDF2` (PDF parsing)
- Optionally: AWS libraries for Bedrock, if adapting

You can install all required packages with:

```bash
pip install -r requirements.txt
```

Sample `requirements.txt`:

```
chromadb
langchain
langchain-community
langchain-chroma
langchain_ollama
fastembed
PyPDF2
```


## Installation

1. **Clone the repository:**

```bash
git clone <YOUR_REPO_URL>
cd Pathology-RAG-Mistral
```

2. **Setup a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # (on Windows: venv\Scripts\activate)
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Install and Start Ollama:**
    - Follow [Ollama's official guide](https://ollama.com/) to download and install Ollama.
    - Download the Mistral model locally:

```bash
ollama pull mistral
```

    - Start Ollama:

```bash
ollama serve
```


## Running the Project

### Step 1: Prepare Data

- Place PDF documents into a folder named `data/`.


### Step 2: Ingest Documents

- To ingest or update the vector database:

```bash
python data.py
# To reset/clear the database:
python data.py --reset
```


### Step 3: Query the System

- Start querying in interactive mode:

```bash
python query_data.py
```

- Enter your questions. Type `quit` or `exit` to leave.


## Project Structure

| File | Purpose |
| :-- | :-- |
| `data.py` | Loads, splits, and ingests PDFs into the vector database |
| `query_data.py` | Interactive query system using RAG and local LLM |
| `get_embedding_function.py` | Sets up the embedding model used for vector search |
| `test_rag.py` | Automated testing of retrieval and answer accuracy |
| `data/` | Folder containing all source documents (PDFs) |
| `chroma/` | Local persistent storage for ChromaDB |

## Usage Examples

**Add new PDFs and re-ingest:**

```bash
python data.py --reset
```

**Query on pathology:**

```
Enter your query: What is the fat/cell ratio in normal adult bone marrow?
```

- The system retrieves relevant passages and generates answers using the local Mistral model.


## Testing

Run the automated test (example in `test_rag.py`):

```bash
python test_rag.py
```

This will check if the RAG pipeline is returning accurate answers for given sample questions.

## Troubleshooting

- Ensure **Ollama** service is running and the **Mistral** model is loaded.
- Confirm PDFs are in the `data/` folder before ingestion.
- To clear and rebuild the vector database, run:

```bash
python data.py --reset
```

- If embeddings are not generated, check the embedding backend and Python module versions.


## Further Reading

- Learn more about [Retrieval Augmented Generation](https://www.pinecone.io/learn/retrieval-augmented-generation/) and [semantic search with vector databases](https://docs.trychroma.com/).
- Explore [Ollama](https://ollama.com/) for running LLMs locally.
- See detailed guides on [ChromaDB](https://docs.trychroma.com/) and its integration with LangChain.

This setup provides a strong local foundation for efficient, private, AI-enabled pathology research and information retrieval.



[^1]: data.py

[^2]: get_embedding_function.py

[^3]: query_data.py

[^4]: test_rag.py

