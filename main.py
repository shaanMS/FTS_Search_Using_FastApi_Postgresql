from fastapi import FastAPI, Depends, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import os

from database import SessionLocal
from crud import fts_search
from schemas import HistoryItem

app = FastAPI(title="Browser History FTS API")

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint - serves the HTML UI
@app.get("/", include_in_schema=False)
async def serve_ui():
    return FileResponse('static/index.html')

# API search endpoint
@app.get("/search", response_model=List[HistoryItem])
def search(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    """
    Live FTS search endpoint.
    Example: /search?q=data+analysis
    """
    results = fts_search(db, q)
    return [{"page_title": r.page_title, "navigated_to_url": r.navigated_to_url} for r in results]

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "FTS Search API is running"}