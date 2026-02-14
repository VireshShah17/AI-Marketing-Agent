# 🚀 Marketing Agent API

A FastAPI-based backend system for managing brands and generating AI-powered marketing content.

This project provides APIs to:

- Create and manage brands
- Generate marketing posts
- Approve and schedule posts
- Manage brand-specific tone and audience targeting

---

## 🧱 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **SQLite** – Database
- **Uvicorn** – ASGI server
- **Python 3.10+**

---

## 📁 Project Structure

```
marketing_agent/
│
├── app/
│   ├── main.py            # FastAPI app entry point
│   ├── models.py          # SQLAlchemy models (Brand, Post)
│   ├── database.py        # Database connection & session
│   ├── routes.py          # API endpoints
│   ├── schemas.py         # Pydantic request/response models
│   ├── services.py        # Business logic (content generation, etc.)
│   └── __init__.py
│
├── venv/                  # Virtual environment (not committed)
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd marketing_agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, generate one:

```bash
pip freeze > requirements.txt
```

---

### 4️⃣ Run the Server

⚠️ IMPORTANT: Run from the project root folder (where `app/` exists)

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Interactive API docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Core API Endpoints

### Brands

- `POST /brands/` → Create brand
- `GET /brands/` → List all brands
- `DELETE /brands/{brand_id}` → Delete brand

### Posts

- `POST /posts/generate/` → Generate post for a brand
- `GET /posts/` → List posts
- `PUT /posts/{post_id}/approve` → Approve post
- `PUT /posts/{post_id}/schedule` → Schedule post

---

## 🗄 Database

- Default: SQLite
- File automatically created (e.g., `marketing.db`)
- SQLAlchemy handles schema creation

---

## 🔁 Development Mode

The `--reload` flag enables:

- Auto-reload when code changes
- Faster development iteration

---

## 🛠 How It Works (High Level)

1. Brands are created with:
   - Name
   - Tone
   - Target Audience

2. When generating a post:
   - Brand tone and audience are injected into content logic
   - Post is saved as `draft`

3. Posts can be:
   - Approved
   - Scheduled
   - Published (future extension)

---

## 📌 Future Improvements

- Authentication (JWT)
- Role-based access
- AI integration (OpenAI API)
- Analytics dashboard
- Docker support
- PostgreSQL production setup

---

## 👨‍💻 Author

Built as a backend-first marketing automation system using FastAPI.

---
