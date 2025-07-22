from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import sqlite3
from pathlib import Path

app = FastAPI()

# Setup database
DATABASE = "contacts.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

# Mount static files and templates
    app.mount("/static", StaticFiles(directory="/Users/maheshyadav/Downloads/PROFILE/frontend/static"), name="static")
templates = Jinja2Templates(directory="/Users/maheshyadav/Downloads/PROFILE/frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit-form")
async def submit_form(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )
    return {"message": "Form submitted successfully"}

if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)
