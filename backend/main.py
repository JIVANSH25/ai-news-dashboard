from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_fetcher import fetch_news
from database import SessionLocal, Favorite
from ai import generate_caption

app = FastAPI()

# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI News Backend Running 🚀"}

@app.get("/news")
def get_news():
    return fetch_news()

@app.post("/favorite")
def add_favorite(item: dict):
    db = SessionLocal()
    fav = Favorite(title=item["title"], link=item["link"])
    db.add(fav)
    db.commit()
    return {"message": "Added to favorites"}

@app.get("/favorites")
def get_favorites():
    db = SessionLocal()
    return db.query(Favorite).all()

@app.post("/broadcast")
def broadcast(item: dict):
    caption = generate_caption(item["title"])
    return {
        "platform": "LinkedIn",
        "caption": caption
    }