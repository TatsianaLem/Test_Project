# User & Order API

This is a simple server-side application built with **FastAPI** and **PostgreSQL** to manage users and their orders.

## ✨ Features

* Create, update, delete, get users
* Create, update, delete, get orders
* Email validation using EmailStr
* Age validation (must be ≥ 0)
* Relational integrity (order must belong to a valid user)
* Dockerized with PostgreSQL
* Clean and modular structure

## 🧱 Tech Stack

* Python 3.10+
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL
* Docker + Docker Compose

## 🔧 Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── schemas.py
│   └── routers
│       ├── __init__.py
│       ├── users.py
│       └── orders.py
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🐳 How to Run with Docker

1. Make sure Docker is installed and running.
2. Clone this repo and navigate to the project folder.
3. Run:

```bash
docker-compose up --build
```

4. Visit the docs:

   * Swagger: http://localhost:8000/docs

## ⚙️ Environment Variables

Create a `.env` file with the following keys (fill in with your own secure values):

```
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DB=<your_database_name>
DATABASE_URL=postgresql://<your_postgres_user>:<your_postgres_password>@db:5432/<your_database_name>
```

## ✅ Example Requests

**Create user:**

```json
POST /users/
{
  "name": "Olga",
  "email": "olga@example.com",
  "age": 25
}
```

**Create order:**

```json
POST /orders/
{
  "title": "New Order",
  "description": "Some description",
  "user_id": 1
}
```
