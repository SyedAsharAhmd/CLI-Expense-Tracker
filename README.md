# Expense Tracker

A full-stack expense tracker: a FastAPI + SQLite backend with a React (Vite) frontend.

## Features

- Add an expense (amount, category, description, date)
- View all expenses
- Filter expenses by category and/or date
- Look up a single expense by ID
- Delete an expense
- Spending summary: total spent, highest expense, totals by category

## Tech stack

- **Backend:** FastAPI, SQLite (`sqlite3`), Pydantic
- **Frontend:** React 19, Vite

## Project structure

```
Expense Tracker/
├── main.py              # FastAPI app and routes
├── database.py          # creates the SQLite expenses table (run on startup)
├── pyproject.toml       # backend dependencies (uv)
└── frontend/            # React + Vite app
    └── src/
        ├── App.jsx
        └── components/
```

## Getting started

### Backend

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run uvicorn main:app --reload --port 8000
```

The API is served at `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The app is served at `http://localhost:5173`.

## API

| Method | Path                        | Description                              |
| ------ | --------------------------- | ----------------------------------------- |
| GET    | `/expenses/view`            | List all expenses                         |
| GET    | `/expenses/summary`         | Total, highest, and per-category totals   |
| GET    | `/expenses/{id}`            | Get a single expense by ID                |
| GET    | `/expenses?category=&date=` | Filter expenses (both params optional)    |
| POST   | `/expenses`                 | Add an expense                            |
| DELETE | `/expenses/{id}`            | Delete an expense                         |

Dates are expected in `DD/MM/YYYY` format.

## Notes

- CORS is configured for the Vite dev server at `http://localhost:5173`.
- `expenses.db` is gitignored — it is created automatically when the API starts.
