import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingManager:
    def __init__(self, model_name):
        self.embedding_model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(self.embedding_model.get_sentence_embedding_dimension())
        self.doc_store = {}
        self.doc_id = 0
    
    def add_document(self, text):
        vector = self.embedding_model.encode([text])[0]
        self.index.add(np.array([vector], dtype=np.float32))
        self.doc_store[self.doc_id] = text
        self.doc_id += 1
        return self.doc_id - 1
    
    def search_documents(self, query, top_k=3):
        query_vector = self.embedding_model.encode([query])[0]
        distances, indices = self.index.search(np.array([query_vector], dtype=np.float32), top_k)
        return [(self.doc_store[i], distances[0][j]) for j, i in enumerate(indices[0]) if i in self.doc_store]
