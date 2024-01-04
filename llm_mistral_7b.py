from llama_index import (
    ServiceContext,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    set_global_service_context,
)
from llama_index.llms import Ollama

def initialize_llm(model_name="mistral"):
    llm = Ollama(model=model_name)
    return llm

def ingest_documents(input_dir, file_extensions, llm, chunk_size=300):
    # Reads PDFs from the specified path
    documents = SimpleDirectoryReader(
        input_dir=input_dir,
        required_exts=file_extensions
    ).load_data()

    # ServiceContext is a bundle of commonly used resources
    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model="local:BAAI/bge-small-en-v1.5",
        chunk_size=chunk_size
    )
    set_global_service_context(service_context)

    # Process documents into nodes
    nodes = service_context.node_parser.get_nodes_from_documents(documents)

    # Store nodes and create indices
    storage_context = StorageContext.from_defaults()
    storage_context.docstore.add_documents(nodes)

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        llm=llm
    )

    return index.as_chat_engine(chat_mode="simple", verbose=True)

def query_chat_engine(chat_engine, query):
    return chat_engine.chat(query)


