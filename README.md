# 🔎 FastSearch – Full Text & Vector Search Application
### FastAPI + PostgreSQL

FastSearch is a high-performance backend search application that fetches
history items from PostgreSQL using full-text and vector search techniques.
This project is designed as a resume-grade, real-world backend system.

---

## 🚀 Features

- Fast full-text / vector-based search
- FastAPI powered backend
- PostgreSQL indexed search
- Clean project architecture
- REST APIs with Swagger docs
- Environment-based configuration

---

## 🧠 Tech Stack

- Backend: FastAPI (Python)
- Database: PostgreSQL
- ORM: SQLAlchemy
- API Docs: Swagger (OpenAPI)
- Tools: Git, Adminer
- OS: Windows / Linux

---

## 📁 Project Structure

FTS_Search_app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── static/
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md

---

## 📸 Screenshots

### 1️⃣ FastSearch Live Application

![FTS Search Live](screenshots/FTS_Search_Live.png)


---

### 2️⃣ PostgreSQL Adminer View

![PostgreSQL Adminer](screenshots/Postgresql_Adminer_View.png)

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| GET | /search | Perform full-text / vector search |
| POST | /add | Insert searchable history data |
| GET | /health | API health check |


---

## ⚙️ Setup Instructions

### Clone Repository
git clone https://github.com/shaanMS/FTS_Search_Using_FastApi_Postgresql.git
cd FTS_Search_app

### Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Environment File (.env)
DATABASE_URL=postgresql://username:password@localhost:5432/fts_db

### Run Application
uvicorn main:app --reload

---

## 🧪 Testing

- APIs tested via Swagger UI
- Search verified with PostgreSQL
- Database inspected using Adminer
- Logs verified via console output

---


## 👨‍💻 Author

Shaan
MCA | Backend & API Developer  
GitHub: https://github.com/shaanMS

---

⭐ Star the repository if you find it useful
