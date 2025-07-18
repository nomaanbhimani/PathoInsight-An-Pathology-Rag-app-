# Pathology-RAG-Mistral

A local Retrieval-Augmented Generation (RAG) system for pathology documents, powered by vector databases ChromaDB and processed with the Mistral language model through Ollama. This project enables efficient search and natural language question-answering over large collections of digital pathology documents.

## 🔬 Project Overview

Pathology-RAG-Mistral leverages modern NLP techniques to let users ask questions about pathology documents. It splits documents, generates vector embeddings for efficient search, and uses a local Mistral LLM (via Ollama) to produce relevant answers based on retrieved context. Everything runs locally, ensuring privacy and control over sensitive medical data.

## 📚 Key Terminology

### Retrieval-Augmented Generation (RAG)
A hybrid system that first retrieves relevant information from a database and then generates answers using a language model, improving accuracy and grounding responses in your actual data.

### ChromaDB (Vector Database)
ChromaDB is a lightweight, fast, and local vector database. It stores document chunks as high-dimensional vectors, enabling efficient similarity search.

### Ollama
A tool for running large language models (like Mistral) locally on your machine, without the need for cloud APIs or internet access.

### Embedding Function
Transforms text (e.g., document chunks and queries) into vector representations. Similar content creates similar vectors, forming the core of the search process.

### Vector Database
A database designed for storing and searching by vector embeddings instead of traditional structured data. Useful for semantic search in NLP applications.

## 🛠️ Requirements

### System Requirements
- Python 3.10 or newer
- pip (Python package manager)
- Pathology PDFs in a data directory for ingestion
- Ollama installed and running with the Mistral model downloaded locally

### Python Packages
```
chromadb
langchain
langchain-community
langchain-chroma
langchain_ollama
fastembed
PyPDF2
```

Optionally: AWS libraries for Bedrock, if adapting for cloud deployment.

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <YOUR_REPO_URL>
cd Pathology-RAG-Mistral
```

### 2. Setup Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
[Pathology-RAG-Mistral.pdf](https://github.com/user-attachments/files/21318607/Pathology-RAG-Mistral.pdf)

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

### 4. Install and Start Ollama
1. Follow [Ollama's official guide](https://ollama.ai) to download and install Ollama
2. Download the Mistral model locally:
   ```bash
   ollama pull mistral
   ```
3. Start Ollama:
   ```bash
   ollama serve
   ```

## 📁 Project Structure

```
Pathology-RAG-Mistral/
├── data.py                      # Loads, splits, and ingests PDFs into vector database
├── query_data.py                # Interactive query system using RAG and local LLM
├── get_embedding_function.py    # Sets up the embedding model for vector search
├── test_rag.py                  # Automated testing of retrieval and answer accuracy
├── data/                        # Folder containing all source documents (PDFs)
├── chroma/                      # Local persistent storage for ChromaDB
└── requirements.txt             # Python dependencies
```

## 🎯 Running the Project

### Step 1: Prepare Data
Place PDF documents into a folder named `data/`.

### Step 2: Ingest Documents
To ingest or update the vector database:
```bash
python data.py
```

To reset/clear the database:
```bash
python data.py --reset
```

### Step 3: Query the System
Start querying in interactive mode:
```bash
python query_data.py
```

Enter your questions about pathology documents. Type `quit` or `exit` to leave.

## 📋 Usage Examples

### Adding New Documents
```bash
# Add new PDFs to data/ folder, then re-ingest
python data.py --reset
```

### Sample Query
```
Enter your query: What is the fat/cell ratio in normal adult bone marrow?
```

### Running Automated Tests
```bash
python test_rag.py
```

This will check if the RAG pipeline is returning accurate answers for given sample questions.

## 🧪 Testing

The system includes automated testing capabilities to verify retrieval and answer accuracy. Run the test suite using:

```bash
python test_rag.py
```

This setup provides a strong local foundation for efficient, private, AI-enabled pathology research and information retrieval.

## 🔧 Troubleshooting

### Common Issues

1. **Ollama Service Not Running**
   - Ensure Ollama service is running and the Mistral model is loaded
   - Check with: `ollama list`

2. **No Documents Found**
   - Confirm PDFs are in the `data/` folder before ingestion
   - Check file permissions

3. **Database Issues**
   - To clear and rebuild the vector database:
     ```bash
     python data.py --reset
     ```

4. **Embedding Generation Problems**
   - Check the embedding backend and Python module versions
   - Verify fastembed installation

## 🔗 Further Reading

- Learn more about [Retrieval Augmented Generation](https://arxiv.org/abs/2005.11401) and semantic search with vector databases
- Explore [Ollama](https://ollama.ai) for running LLMs locally
- See detailed guides on [ChromaDB](https://docs.trychroma.com/) and its integration with [LangChain](https://python.langchain.com/docs/get_started/introduction)

## 🛡️ Privacy & Security

This system runs entirely locally, ensuring that sensitive medical data never leaves your machine. All processing, including document ingestion, vector storage, and query answering, happens on your local infrastructure.

