# Full Stack Flask + React + SQL App

This project is a full-stack web application with:
- Flask as the backend (Python)  
- React as the frontend (JavaScript)  
- SQLite as the database  

The repository is organized into two main folders:  
- `backend/` — Flask server & database  
- `frontend/` — React app

---

## Backend Setup (Flask + SQLite)

### 1. Create and activate a virtual environment
```bash
cd backend
python -m venv venv

#### macOS / Linux
source venv/bin/activate

#### Windows (PowerShell)
venv\Scripts\Activate.ps1

#### Go back to main directory or copy requirment.txt here
cd ..

#### Instal dependencies
pip install -r requirements.txt

#### From backend folder run
python main.py

#### Default URL
http://127.0.0.1:5000

## Frontend Setup (React + Vite)
cd frontend

#### Install server
npm install

#### start server
npm run dev

#### Defualt URL
http://localhost:5173


# How to run the application

1. Copy paste the URL: http://localhost:5173
2. Make sure backend is also running
3. It automatically generates the SQL data in background on first run, if it doesn't press Generate Data, with link already given or use https://pokeapi.co/api/v2/pokemon/ (If you generate again, it will take 10 to 20 sec just wait and it will show alert that data is complete)
4. It will show original table.
5. You can add any SQL query in box and press send query, to run the query on data
6. Or you can press Generate button to show the question asked in challenge.





