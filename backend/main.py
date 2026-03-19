from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

from backend.news_fetcher import fetch_news
from backend.database import SessionLocal, Favorite
from backend.ai import generate_caption

app = FastAPI()

# ✅ CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Serve Frontend UI
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ✅ Fetch news
@app.get("/news")
def get_news():
    return fetch_news()

# ✅ Add to favorites
@app.post("/favorite")
def add_favorite(item: dict):
    db = SessionLocal()
    fav = Favorite(title=item["title"], link=item["link"])
    db.add(fav)
    db.commit()
    return {"message": "Added to favorites"}

# ✅ Get favorites
@app.get("/favorites")
def get_favorites():
    db = SessionLocal()
    return db.query(Favorite).all()

# ✅ AI Broadcast
@app.post("/broadcast")
def broadcast(item: dict):
    caption = generate_caption(item["title"])
    return {
        "platform": "LinkedIn",
        "caption": caption
    }