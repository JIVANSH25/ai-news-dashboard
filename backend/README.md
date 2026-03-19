# 🧠 AI News Aggregation & Broadcasting Dashboard

## 🚀 Overview

This project is an AI-powered News Aggregation Dashboard that collects, processes, and displays the latest AI-related news from multiple sources. It allows users to explore news, save favorites, and generate AI-style broadcast content for sharing.

---

## ✨ Features

### 📰 News Aggregation

* Fetches AI news from multiple sources (TechCrunch, OpenAI Blog, etc.)
* Displays structured data: Title, Summary, Link, Published Date

### ⭐ Favorites System

* Save important news items
* Persistent storage using SQLite database
* Retrieve saved favorites anytime

### 📣 AI Broadcast Feature

* Generate LinkedIn-style posts from news titles
* Simulated AI layer (easily replaceable with real LLM APIs)

### 🎨 Interactive Dashboard

* Clean UI using HTML, CSS, and JavaScript
* Displays news cards with actions:

  * Read More
  * Add to Favorites
  * Broadcast

---

## 🏗️ Architecture

```
RSS Feeds → Fetcher → Backend (FastAPI) → Database → API → Frontend UI
                                      ↓
                                 AI Layer (Caption Generator)
```

---

## 🧰 Tech Stack

| Layer      | Technology Used                    |
| ---------- | ---------------------------------- |
| Backend    | FastAPI (Python)                   |
| Frontend   | HTML, JavaScript                   |
| Database   | SQLite (SQLAlchemy)                |
| AI Layer   | Mock AI (extendable to OpenAI API) |
| Deployment | Render (recommended)               |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/JIVANSH25/ai-news-dashboard.git
cd ai-news-dashboard
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend Server

```
cd backend
uvicorn main:app --reload
```

---

### 5️⃣ Run Frontend

* Open `frontend/index.html` in browser

---

## 🌐 API Endpoints

| Endpoint     | Method | Description         |
| ------------ | ------ | ------------------- |
| `/news`      | GET    | Fetch AI news       |
| `/favorite`  | POST   | Save a news item    |
| `/favorites` | GET    | Get saved favorites |
| `/broadcast` | POST   | Generate AI caption |

---

## 🧠 AI Integration

Currently, the AI layer uses a **mock caption generator** to simulate LinkedIn-style posts.
This can be easily upgraded to real LLM APIs such as:

* OpenAI GPT
* Google Gemini
* Anthropic Claude

---

## 🚀 Deployment

The project can be deployed using:

* Render
* Fly.io
* AWS

### Example Start Command:

```
uvicorn backend.main:app --host 0.0.0.0 --port 10000
```

---

## 📦 Deliverables

* ✔ Backend API (FastAPI)
* ✔ News ingestion system
* ✔ Favorites & database integration
* ✔ AI broadcast feature
* ✔ Frontend dashboard
* ✔ Deployment-ready setup

---

## 💡 Future Improvements

* Real-time AI summarization using LLMs
* News deduplication using embeddings
* User authentication system
* Advanced UI (React/Next.js)
* Analytics dashboard (trending topics)

---

## 👨‍💻 Author

Developed as part of a GenAI Internship Assignment.

---

## ⭐ Acknowledgment

This project demonstrates practical implementation of:

* AI-powered workflows
* Full-stack development
* Scalable backend architecture
