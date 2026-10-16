# Python PostgreSQL Student Management System

A menu-driven Python application that interacts with a PostgreSQL database using the `psycopg2` library. This project demonstrates basic CRUD operations, dynamic user inputs using parameterized queries, and PostgreSQL database management directly through Python scripts.

## 📋 Features

* **Database & Table Setup:** Auto-checks and creates the `students` table if missing.
* **Dynamic Data Insertion:** Accepts user inputs interactively from the terminal to insert records using parameterized SQL queries (`%s`) to protect against SQL Injection.
* **Data Retrieval:**
  * Displays single records using `fetchone()`.
  * Displays all student records stored in the database.
  * Queries records filtered by specific criteria (`WHERE` clause).
* **Table Truncation:** Allows clearing all records and resetting table primary key IDs (`TRUNCATE TABLE RESTART IDENTITY`).
* **Interactive Menu:** Menu-driven terminal interface built using Python's `match-case` control flow.

## 🛠️ Prerequisites & Installation

Ensure you have the following installed on your system:

* **Python 3.10+** (Required for `match-case` syntax)
* **PostgreSQL Server** (PostgreSQL 18 or lower)
* **psycopg2-binary** library

### Install Required Python Library

Run the following command in your terminal:

```bash
pip install psycopg2-binary
```

## ⚙️ Database Configuration

Before running the application:

1. Ensure PostgreSQL service is running on your machine.
2. Ensure the target database (`students_db`) exists. You can create it in `psql` using:

```sql
CREATE DATABASE students_db;
```

3. Open `main.py` and update the `DB_PARAMS` dictionary with your local PostgreSQL credentials:

```python
DB_PARAMS = {
    "dbname": "students_db",
    "user": "postgres",
    "password": "YOUR_POSTGRES_PASSWORD",
    "host": "localhost",
    "port": "5432"
}
```

## 🚀 How to Run the Application

Execute the Python script using your terminal:

```bash
python main.py
```

### Main Menu Options:

```text
========================================
      POSTGRESQL DATABASE OPERATIONS
========================================
1. Insert Student Record (Dynamic Input)
2. Display First Record (fetchone)
3. Display All Records
4. Search Students by Course (WHERE Clause)
5. Truncate Table
6. Exit
========================================
```

## 📁 Repository Structure

```text
Python-PostgreSQL-Student-Management/
│
├── main.py            # Main application source code
├── database.sql       # PostgreSQL database export dump file
├── README.md          # Project documentation
└── .gitignore         # File to ignore unnecessary Python cache files
```

## 💾 Generating Database Dump (`database.sql`)

To export your database schema and data into a `.sql` dump file for submission or GitHub:

```powershell
& "C:\Program Files\PostgreSQL\18\bin\pg_dump.exe" -U postgres -d students_db > database.sql
```
