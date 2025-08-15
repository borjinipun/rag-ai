# Document Q&A LLM Application with Docker & Hugging Face

A step-by-step guide to building and deploying a **Document Question-Answering Chatbot** using **Gradio**, **LlamaIndex**, **LlamaParse**, **Mixedbread AI**, **Groq**, **Docker**, and **Hugging Face Spaces**.

---

## 📌 Project Overview
This project demonstrates how to:
- Build an **RAG (Retrieval-Augmented Generation)** based chatbot that allows users to upload documents and query them in real time.
- Integrate multiple AI services for parsing, embedding, and inference.
- Package and deploy the application using **Docker** to **Hugging Face Spaces**.

### **Tools Used**
- **Gradio** – UI for document upload & chat
- **LlamaCloud / LlamaParse** – Parse multiple document formats
- **Mixedbread AI** – Generate document & query embeddings
- **Groq** – Access high-speed LLM responses (`llama-3.1-70b-versatile`)
- **LlamaIndex** – Orchestrate RAG pipeline
- **Docker** – Containerization
- **Hugging Face Spaces** – Cloud deployment

---

## 📂 Project Structure
├── app.py # Main application
├── requirements.txt # Python dependencies
├── Dockerfile # Container setup
├── .env # API keys (Not committed to Git)
└── .gitignore # Ignore sensitive files


---

## 🔑 Prerequisites
- **Python 3.9+**
- **Docker**
- API Keys:
  - LlamaCloud
  - Mixedbread AI
  - Groq Cloud

