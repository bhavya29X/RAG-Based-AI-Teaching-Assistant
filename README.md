# RAG-Based-AI-Teaching-Assistant
End-to-end RAG-based AI Teaching Assistant that converts educational videos into a searchable knowledge base using Whisper, vector embeddings, and LLMs.
---

## 📌 Project Overview

This project demonstrates how real-world AI assistants are built by combining:

* Speech-to-text
* Semantic embeddings
* Vector-based retrieval
* Large Language Models (LLMs)

The assistant learns directly from video content and generates accurate, context-aware responses.

---

## ⚙️ Architecture & Workflow

1. **Video Collection**

   * Collected 20+ educational videos

2. **Video → Audio Conversion**

   * Converted videos to MP3 using **FFmpeg** and Python’s `subprocess` module

3. **Speech-to-Text**

   * Transcribed audio into structured JSON files using **Whisper (large-v2)**

4. **Chunking & Embeddings**

   * Created single-line transcript chunks
   * Merged **5 lines into one semantic chunk** to improve retrieval quality
   * Generated vector embeddings using **all-MiniLM**

5. **Retrieval & Response Generation**

   * Retrieved relevant chunks based on user query
   * Generated final responses using **LLaMA 3.2**
   * Pipeline supports **GPT-5** (not used due to hardware limitations)

---

## 🛠️ Tech Stack

* **Python**
* **FFmpeg**
* **Whisper (large-v2)**
* **all-MiniLM embeddings**
* **LLaMA 3.2**
* **Vector Search / RAG Pipeline**

---

## 📈 Key Features

* End-to-end RAG pipeline
* Improved answer quality using smart chunk merging
* Model-agnostic design (easy LLM replacement)
* Practical, real-world AI system implementation

---

## 🧠 Learnings & Outcomes

* Deep understanding of **RAG-based systems**
* Experience with **audio processing, embeddings, and LLMs**
* Insight into optimizing chunking strategies
* Hands-on AI system design beyond prompt engineering

---

## 🚀 Future Improvements

* Integrate **GPT-5** with higher hardware capacity
* Add a vector database (FAISS / Chroma / Pinecone)
* Build a web interface (Streamlit / Flask)
* Add conversation memory

---

## 🤝 Connect

LinkedIn: [https://www.linkedin.com/in/bhavya-shah-622a9a271/](https://www.linkedin.com/in/bhavya-shah-622a9a271/)
Email: [bhavya29shah10@gmail.com](bhavya29shah10@gmail.com)

