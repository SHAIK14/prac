# Live Stock Trading Dashboard — Setup

## Backend (FastAPI)

```bash
mkdir trading-dashboard && cd trading-dashboard
mkdir backend && cd backend

python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn

# create main.py, then run the dev server:
uvicorn main:app --reload --port 8000
```

- `--reload` auto-restarts the server on code changes (dev only, remove for prod).
- Server runs at `http://localhost:8000`.
- Interactive API docs auto-generated at `http://localhost:8000/docs`.

## Frontend (React)

```bash
cd trading-dashboard

# using Vite (faster, recommended over create-react-app)
npm create vite@latest frontend -- --template react
cd frontend
npm install

npm run dev
```

- Dev server runs at `http://localhost:5173` by default.
- To call the FastAPI backend from React during dev without CORS issues, either:
  - add `CORSMiddleware` in FastAPI allowing `http://localhost:5173`, or
  - set up a Vite proxy in `vite.config.js` pointing `/api` → `http://localhost:8000`.

## Folder structure (target)

```
trading-dashboard/
├── backend/
│   ├── venv/
│   ├── main.py
│   └── ...
└── frontend/
    ├── src/
    └── ...
```
