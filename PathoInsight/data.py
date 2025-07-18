import shutil
import chromadb
import os
import argparse
from get_embedding_function import get_embedding_function
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
DATA_PATH="data"
CHROMA_PATH="chroma"
def main():

    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.
    documents = load_document()
    chunks = split_document(documents)
    add_to_chroma(chunks)


def load_document():
    
    doc_loader=PyPDFDirectoryLoader(DATA_PATH)
    return doc_loader.load()
'''document=load_document()
print(document[0])'''


def split_document(documents:list[Document]):
    text_splitter=RecursiveCharacterTextSplitter( 
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
        )
    return text_splitter.split_documents(documents)
'''documents=load_document()
chunks=split_document(documents)
print(chunks[0])'''
def calculate_chunk_ids(chunks):
    last_page_id=None
    current_chunk_index=0
    for chunk in chunks:
        source=chunk.metadata.get("source")
        page=chunk.metadata.get("page")
        current_page_id=f"{source}:{page}"
        if current_page_id==last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0
        chunk_id=f'{current_page_id}:{current_chunk_index}'
        last_page_id=current_page_id

        chunk.metadata['id']=chunk_id
    return chunks


def add_to_chroma(chunks:list[Document],batch_size=5000):
    db=Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )
    

    chunks_with_ids=calculate_chunk_ids(chunks)
    existing_items=db.get(include=[])
    existing_ids=set(existing_items['ids'])
    print(f"Number of existing documents in DB: {len(existing_ids)}")
 
    new_chunks=[]
    for chunk in chunks_with_ids:
        if chunk.metadata['id'] not in existing_ids:
            new_chunks.append(chunk)
    if len(new_chunks):
        print(f"Adding {len(new_chunks)} new chunks to the database.")
        new_chunk_ids=[chunk.metadata['id'] for chunk in new_chunks]
        db.add_documents(new_chunks)
        db.persist()
    else:
     print("No new chunks to add to the database.")

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


if __name__ == "__main__":
    main()



