Strucutre of Project
rag_project/
│── data/                      # Stores generated responses and document data
│── src/                       # Source code directory
│   │── __init__.py            # Makes src a package
│   │── config.py              # Configuration settings (API keys, model names, etc.)
│   │── embedding.py           # Handles text embedding and vector search
│   │── groq_api.py            # Handles Groq API calls
│   │── rag.py                 # Main RAG system logic
│   │── main.py                # Entry point for running the application
│── requirements.txt           # Required dependencies
│── README.md                  # Documentation about the project
│── .gitignore                 # Files to ignore in version control
