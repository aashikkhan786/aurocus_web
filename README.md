# Aurocous — Premium Corporate Website

A modern, high-performance corporate website for **Aurocous**, a forward-thinking technology company specializing in IT services, custom software development, and independent digital product innovation.

## Tech Stack

- **Backend:** Python 3.14+ · FastAPI · Uvicorn
- **Templating:** Jinja2
- **Database:** SQLite (via Python's built-in `sqlite3`)
- **Validation:** Pydantic v2 · email-validator
- **Frontend:** Vanilla HTML/CSS/JS · Google Fonts (Manrope, Inter)
- **Testing:** pytest · httpx

## Features

- Fully responsive single-page corporate website
- Smooth scroll anchor navigation across all sections
- Dynamic service, industry, and product showcases
- Animated statistics counters
- Secure contact form with CSRF protection and honeypot spam filtering
- Contact inquiries stored in SQLite
- SEO-optimized with meta tags, Open Graph, robots.txt, and sitemap.xml
- Accessible and semantic HTML5

## Prerequisites

- **Python 3.14** or higher
- **pip** package manager
- **Git**

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/aurocous.git
   cd aurocous
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set a strong `SECRET_KEY`.

5. **Run the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Visit the site**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Project Structure

```
aurocous/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py             # Settings via pydantic-settings
│   ├── database.py           # SQLite database helpers
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── pages.py          # Page routes (home, robots, sitemap)
│   │   └── contact.py        # Contact form submission
│   ├── services/
│   │   ├── __init__.py
│   │   └── content.py        # Static content data provider
│   ├── templates/
│   │   └── index.html        # Main Jinja2 template
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── images/
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Test fixtures and configuration
│   ├── test_main.py          # Homepage and static route tests
│   └── test_contact.py       # Contact form tests
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Running Tests

```bash
pytest
```

With verbose output:

```bash
pytest -v
```

With coverage:

```bash
pytest --cov=app --cov-report=html
```

## License

All rights reserved. © Aurocous.
