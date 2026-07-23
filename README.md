# 💰 Expense Tracker API

A secure, scalable, and RESTful Expense Tracker API built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

This project enables users to securely manage their personal expenses through JWT-based authentication while providing powerful features such as searching, filtering, sorting, pagination, and expense analytics.

Designed with modern backend development best practices, the API demonstrates authentication, database relationships, request validation, RESTful API design, and automatic API documentation.

---

# 🚀 Features

## 🔐 Authentication

* User Registration
* Secure User Login
* JWT (JSON Web Token) Authentication
* Password Hashing with Passlib
* Protected Routes

## 💳 Expense Management

* Create Expenses
* View Expenses
* Update Expenses
* Delete Expenses

## 🔍 Search & Filtering

* Search expenses by title
* Filter expenses by category
* Pagination using `skip` and `limit`
* Sort expenses by:

  * Amount
  * Title
  * Date Created

## 📊 Analytics

* Total number of expenses
* Total amount spent
* Average expense
* Category-wise expense summary

## 📄 API Documentation

* Interactive Swagger UI
* ReDoc Documentation

---

# 🛠️ Tech Stack

## Backend

* Python 3.10+
* FastAPI

## Database

* SQLite
* SQLAlchemy ORM

## Authentication & Security

* JWT Authentication
* OAuth2 Password Flow
* Passlib
* Python-Jose

## Data Validation

* Pydantic

## Development Tools

* Git
* GitHub
* VS Code
* Uvicorn
* Postman

---

# 📁 Project Structure

```text
expense-tracker-api/
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Folder Overview

| File        | Description                                |
| ----------- | ------------------------------------------ |
| main.py     | FastAPI application and API routes         |
| models.py   | SQLAlchemy database models                 |
| schemas.py  | Pydantic request and response models       |
| database.py | Database connection and session management |
| auth.py     | JWT token creation and authentication      |
| security.py | Password hashing and verification          |

---

# ⚙️ Installation & Setup

## Clone the Repository

```bash
git clone https://github.com/Kikobazz123/expense-tracker-api.git
```

## Navigate into the Project

```bash
cd expense-tracker-api
```

## Requirements

* Python 3.10+
* Git
* pip

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

The application will start at:

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```


Lordmark Dorgu
=======
| Method | Endpoint  | Description         |
| ------ | --------- | ------------------- |
| GET    | /         | API Health Check    |
| POST   | /register | Register a New User |
=======
```
http://127.0.0.1:8000/redoc
```


---

# 🔐 Authentication

The API uses **JWT Authentication**.

### Register


GitHub: https://github.com/Kikobazz123

=======
```
POST /register
```

Create a user by providing:

* Username
* Email
* Password

---

### Login

```
POST /login
```

Login using your email and password.

Example Response

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

### Access Protected Routes

1. Login.
2. Copy the access token.
3. Open Swagger.
4. Click **Authorize**.
5. Enter:

```
Bearer your_access_token
```

6. Click **Authorize**.

---

# 📌 API Endpoints

| Method | Endpoint            | Description              | Authentication |
| ------ | ------------------- | ------------------------ | -------------- |
| GET    | /                   | API Health Check         | ❌              |
| POST   | /register           | Register User            | ❌              |
| POST   | /login              | Login User               | ❌              |
| GET    | /me                 | Get Current User         | ✅              |
| POST   | /expenses           | Create Expense           | ✅              |
| GET    | /expenses           | Retrieve Expenses        | ✅              |
| PUT    | /expenses/{id}      | Update Expense           | ✅              |
| DELETE | /expenses/{id}      | Delete Expense           | ✅              |
| GET    | /summary            | Expense Summary          | ✅              |
| GET    | /summary/categories | Category Expense Summary | ✅              |

---

# 📸 Screenshots

## Swagger Documentation

> Add a screenshot of your Swagger UI here.

Example:

```
docs/swagger-home.png
```

---

## Expense Endpoints

> Add screenshots demonstrating CRUD operations.

---

# 🔮 Future Improvements

* PostgreSQL Support
* Docker Containerization
* Environment Variables (.env)
* Alembic Database Migrations
* CSV Export
* PDF Report Generation
* Monthly Expense Reports
* Budget Management
* Recurring Expenses
* Unit & Integration Tests
* Cloud Deployment (Render)

---

# 👨‍💻 Author

**Lordmark Ebimobowei Dorgu (Kikobazz)**

**Backend Developer | API Developer | AI Automation Enthusiast | Blockchain Developer**

GitHub:
https://github.com/Kikobazz123

Upwork:
https://www.upwork.com/freelancers/~018e0b876222790b59?mp_source=share

Email:
[zaxellimited360@gmail.com](mailto:zaxellimited360@gmail.com)

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.

