from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

fake_db = [
    {
        "id": 1,
        "title": "The Architecture of Silence: Navigating the New Minimalism "
        "in Urban Design.",
        "excerpt": "As cities grow louder, a new generation of architects "
        "is prioritizing acoustic serenity and visual void. We examine the "
        "structural shift toward environments that demand nothing but your "
        "attention.",
        "published_at": "2026-06-24 20:00:00",
        "author": "John Doe",
        "read_duration": 8
    },
    {
        "id": 2,
        "title": "The Architecture of FastAPI",
        "excerpt": "As cities grow louder, a new generation of architects "
        "is prioritizing acoustic serenity and visual void. We examine the "
        "structural shift toward environments that demand nothing but your "
        "attention.",
        "published_at": "2026-06-27 20:00:00",
        "author": "Jane Doe",
        "read_duration": 8
    }
]


@app.get("/articles")
def list_articles():
    return fake_db


@app.get("/articles/{article_id}")
def get_article(article_id: int): # pour recuperer les articles sous forme d'un entier
    for item in fake_db:
        if item["id"] == article_id:
            return item
        
    raise HTTPException(
        status_code=404,
        detail="Article introuvable"
    )