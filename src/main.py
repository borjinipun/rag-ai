import sys
from pathlib import Path
from src.rag import RAGSystem
sys.path.append(str(Path(__file__).resolve().parent))

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

rag = RAGSystem()
docs = [
    "Machine learning is a method of data analysis that automates analytical model building.",
    "Deep learning is a subset of machine learning that uses neural networks with three or more layers.",
    "Reinforcement learning is an area of machine learning concerned with how intelligent agents take actions."
]

for doc in docs:
    rag.add_document(doc)

query = "What is deep learning?"
response = rag.generate_response(query)

# Save response to a file
response_file = DATA_DIR / "response.txt"
with response_file.open("w") as f:
    f.write(response)

print(f"Response saved to {response_file}")