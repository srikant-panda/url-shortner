# ✂️ Snip.ly — URL Shortener

A fast, modern URL shortener built with **FastAPI** and a sleek animated frontend.

![Python](https://img.shields.io/badge/Python-3.10+-7c3aed?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-06b6d4?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-f59e0b?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-10b981?style=flat-square)

---

## ✨ Features

- 🔗 Shorten any URL instantly
- ⚡ Instant redirect via short code
- 🎨 Animated glassmorphism UI (mesh gradients, floating orbs, particles)
- 📋 Recent links history stored in `localStorage`
- 📱 Fully responsive (mobile-friendly)
- 🔒 CORS-enabled REST API

---

## 🗂️ Project Structure

```
url_shortener/
├── main.py               # FastAPI app entry point
├── db.py                 # Database setup (SQLAlchemy)
├── utils.py              # Short code generator
├── api/
│   └── routes.py         # API route definitions
├── models/
│   └── url.py            # SQLAlchemy URL model
├── schemas/
│   └── url_schema.py     # Pydantic request/response schemas
├── services/
│   └── url_service.py    # Business logic
└── static/
    ├── index.html        # Animated frontend
    └── favicon.svg       # SVG favicon
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/srikant-panda/url-shortner.git
cd url-shortner
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy aiofiles
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

Open **http://localhost:8000** in your browser.

---

## 📡 API Reference

### `POST /shorten`

Shorten a long URL.

**Request body:**
```json
{ "url": "https://example.com/very/long/path" }
```

**Response:**
```json
{
  "id": 1,
  "url": "https://example.com/very/long/path",
  "short_code": "aB3xYz"
}
```

---

### `GET /{code}`

Redirects to the original URL associated with the short code.

| Status | Meaning |
|--------|---------|
| `307`  | Redirect to original URL |
| `404`  | Short code not found |

---

## 🖥️ Frontend

The frontend is a single-file vanilla HTML/CSS/JS app served at `/`.

**UI highlights:**
- Animated mesh gradient background
- Floating glowing orbs & rising particle field
- Glassmorphism card with spring animations
- Copy-to-clipboard with visual feedback
- Link history persisted in `localStorage`

---

## 🛠️ Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Backend   | FastAPI, Python     |
| ORM       | SQLAlchemy          |
| Database  | SQLite (default)    |
| Frontend  | HTML, CSS, Vanilla JS |
| Server    | Uvicorn             |

---

## 📄 License

MIT © [srikant-panda](https://github.com/srikant-panda)
