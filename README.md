# Expense Tracker API

Secure Expense Tracker REST API built with FastAPI, SQLAlchemy, JWT Authentication, and SQLite.

## 🚀 Features

* User Registration API
* FastAPI REST Architecture
* SQLite Database Integration
* SQLAlchemy ORM
* Pydantic Data Validation
* Interactive Swagger API Documentation

## 🛠 Tech Stack

* Python 3.10
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## 📂 Project Structure

```text
expense-tracker-api/
│
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Kikobazz123/expense-tracker-api.git
```

Move into the project:

```bash
cd expense-tracker-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## 📌 Current Endpoints

| Method | Endpoint  | Description         |
| ------ | --------- | ------------------- |
| GET    | /         | API Health Check    |
| POST   | /register | Register a New User |

## 🔨 Planned Features

* Password Hashing (bcrypt)
* JWT Authentication
* Login Endpoint
* Expense CRUD
* Expense Categories
* Monthly Reports
* Docker Support
* Deployment to Render

## 👨‍💻 Author

**Lordmark Dorgu aka Kikobazz**

GitHub: https://github.com/Kikobazz123
