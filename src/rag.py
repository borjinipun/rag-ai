from src.embedding import EmbeddingManager
from src.groq_api import GroqAPI
from src.config import MODEL_NAME

class RAGSystem:
    def __init__(self):
        self.embedding_manager = EmbeddingManager(MODEL_NAME)
    
    def add_document(self, text):
        return self.embedding_manager.add_document(text)
    
    def generate_response(self, query):
        retrieved_docs = self.embedding_manager.search_documents(query)
        context = "\n".join([doc for doc, _ in retrieved_docs])
        full_prompt = f"Context:\n{context}\n\nUser Query: {query}\n\nResponse:"
        return GroqAPI.query(full_prompt)