'''from langchain_ollama.embeddings import OllamaEmbeddings
def get_embedding_function():
        embeddings = OllamaEmbeddings(model="mistral")
        return embeddings'''
from langchain_community.embeddings.bedrock import BedrockEmbeddings

def get_embedding_function():
    '''embeddings = BedrockEmbeddings(
        credentials_profile_name="default", region_name="us-east-1"
    )'''
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
    embeddings = FastEmbedEmbeddings()

    return embeddings