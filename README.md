# 🩸 Blood Bank API

A high-performance backend API for managing blood donation and request operations. Built with **FastAPI** for blazing-fast APIs, **PostgreSQL** for reliable data storage, and **Redis** for smart caching to enhance response speed.

---

## 🚀 Features

- 💉 Blood donation and request management
- 📝 Submit forms to donate or request blood
- 🗃️ PostgreSQL for persistent data storage
- ⚡ Redis integration for fast access to cached data
- 🔐 Admin authentication using JWT tokens

---

## 🧰 Technologies Used

| Tool | Description |
|------|-------------|
| <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="20"/> **FastAPI** | Python framework for building APIs |
| <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Redis_Logo.svg/1200px-Redis_Logo.svg.png" alt="Redis" width="20"/> **Redis** | In-memory database used for caching |
| 🐘 **PostgreSQL** | Relational database for data storage |
| 🔐 **JWT (JOSE)** | Secure token-based authentication |

---

## 📦 Project Structure

backend/
├── app/
│ ├── models/ # SQLAlchemy models
│ ├── routes/ # API routes
│ ├── schemas/ # Pydantic schemas
│ └── utils.py # Utility functions (JWT, Redis)
├── .env # Environment variables (ignored by Git)
├── .gitignore
├── main.py # Entry point
└── requirements.txt



## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/CodeWithAzlo/bloodbank-fastapi
cd blood-bank-api/backend

