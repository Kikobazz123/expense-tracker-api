# Expense Tracker API

## Features

- User Registration
- JWT Authentication
- Password Hashing
- User Login
- Protected Routes
- Create Expenses
- View Expenses
- Update Expenses
- Delete Expenses
- SQLite Database
- SQLAlchemy ORM

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Passlib
- JWT
- Uvicorn

## Installation

```bash
git clone https://github.com/Kikobazz123/expense-tracker-api.git
cd expense-tracker-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## API Documentation

```
http://127.0.0.1:8000/docs
```

## Author


Lordmark Dorgu
=======
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

