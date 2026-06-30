# Flask-SQLAlchemy Demo

This project demonstrates how to use Flask with SQLAlchemy to create a simple web app, define models (`Book`, `Reader`, `Review`), and persist/query data in a SQLite database.

---

## 🚀 Setup Instructions

### 1. Clone or Download the Project

```bash
cd C:\Directory\Projects\ML_Repo\Flask
```

### 2. Create a Virtual Environment

```powershell
python -m venv Flask-SQLAlchemy
```

### 3. Activate the Virtual Environment

**PowerShell:**
```powershell
.\Flask-SQLAlchemy\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
.\Flask-SQLAlchemy\Scripts\activate.bat
```

Your prompt should now show `(Flask-SQLAlchemy)`.

---

## 📦 Install Dependencies

```powershell
pip install flask flask_sqlalchemy
```

---

## 🏗️ Run the Flask App

Start the server:

```powershell
python app.py
```

You should see output like:

```
* Running on http://127.0.0.1:5000
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to see the home page.

---

## 💾 Create Database and Objects

The database (`myDB.db`) is created automatically when you run `app.py` with:

```python
with app.app_context():
    db.create_all()
```

To insert sample objects, run:

```powershell
python create_object.py
```

If successful, you'll see:

```
Objects committed successfully!
```

---

## 🔍 Query the Database

You can query inside a Python REPL:

```powershell
python
```

Then:

```python
from app import app, db, Book, Reader, Review

with app.app_context():
    print(Book.query.all())
    print(Reader.query.all())
    print(Review.query.all())
```

---

## 🌐 Extra Routes

Add routes in `app.py` to view data in the browser:

```python
@app.route('/books')
def show_books():
    books = Book.query.all()
    return "<br>".join([b.title for b in books])
```

Visit [http://127.0.0.1:5000/books](http://127.0.0.1:5000/books) to see all book titles.

---

## ⚠️ Common Issues

- **Working outside of application context** → Wrap DB operations in:
  ```python
  with app.app_context():
      # db operations here
  ```

- **UNIQUE constraint failed** → Don't hard-code IDs. Let SQLAlchemy auto-generate them.

- **PowerShell errors with `print(...)`** → Run Python code inside the REPL (`python`), not directly in PowerShell.

---

## ✅ Summary

1. Create & activate venv
2. Install Flask + SQLAlchemy
3. Run `app.py` → starts server & creates DB
4. Run `create_object.py` → inserts sample data
