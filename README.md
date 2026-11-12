# 🌊 FloatChat – AI-Powered Conversational Interface for ARGO Ocean Data 🌐

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![React](https://img.shields.io/badge/react-18.0-blue?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-async%20framework-green?logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## 🚀 Project Overview
**FloatChat** is an **AI-powered conversational system** that makes complex **ARGO ocean float data** accessible to everyone through a natural language interface.  
It combines **LLMs + RAG pipelines + interactive dashboards** to let users ask questions like:  
- *“Show me salinity profiles near the equator in March 2023”*  
- *“Compare BGC parameters in the Arabian Sea for the last 6 months”*  
- *“What are the nearest ARGO floats to this location?”*  

This project is built for **Smart India Hackathon (SIH) 2025** under the **Ministry of Earth Sciences (MoES), INCOIS**.

---

## 🏗️ Tech Stack

### 🌐 Frontend
- **React 18 + Vite** – Modern UI framework  
- **Tailwind CSS** – Styling & responsive design  
- **Plotly.js / Recharts** – Data visualization  
- **Leaflet / Mapbox** – Geospatial mapping  
- **Axios** – API integration  

### ⚙️ Backend
- **FastAPI** – Async Python backend  
- **PostgreSQL** – Structured storage (ARGO NetCDF → SQL)  
- **Chroma / FAISS** – Vector database for embeddings & RAG  
- **LangChain / LlamaIndex** – Query pipeline (NL → SQL + response)  
- **xarray, netCDF4** – Scientific data parsing  
- **PyJWT** – Authentication (demo)  

---

## 📂 Project Structure
floatchat-argo/
├── frontend/ # React app (UI)
├── backend/ # FastAPI app (APIs, RAG, DB)
├── docs/ # Diagrams, architecture
├── README.md # Project overview
└── .gitignore


## ⚡ Setup Instructions

### 🔹 Frontend
```bash
cd frontend
npm install
npm run dev
🔹 Backend
bash
Copy code
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
🔹 Access
Frontend: http://localhost:5173/

Backend API docs: http://localhost:8000/docs

📊 Features
✅ Ingest ARGO NetCDF data → SQL + VectorDB
✅ Natural language → SQL queries via LLM (RAG pipeline)
✅ Interactive dashboard with maps & plots
✅ Chatbot interface for query discovery
✅ Extensible to BGC floats, gliders, buoys, satellite data

📌 Roadmap
 Data ingestion (NetCDF → PostgreSQL)

 Vector DB setup with embeddings

 Chatbot integration with RAG pipeline

 Interactive dashboard (Leaflet + Plotly)

 Authentication (JWT demo)

 Deployment (Docker + Cloud)

🔍 Dataset Sources
🌐 Argo Global Data Repository

🌊 Indian Argo Project (INCOIS)

👥 Team Roles
Data/Backend Lead → Python, FastAPI, NetCDF, RAG

Frontend Lead → React, UI/UX, charts, maps

AI/ML Engineer → LLM fine-tuning, embeddings, RAG pipeline

DevOps/Integrator → GitHub, Docker, deployment, docs

🏆 Hackathon Relevance
Makes complex ocean data accessible to scientists, policymakers, students

Aligns with Digital India + Blue Economy initiatives

Bridges domain knowledge gap via conversational AI

