from fastapi import FastAPI

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
    }
]


@app.get("/articles")
def list_articles():
    return fake_db
