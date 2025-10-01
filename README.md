# User Management System

A simple Python project demonstrating user management with **PostgreSQL** and **bcrypt** for password hashing.  
Users can be added and their passwords are stored securely in the database. Includes timestamping for account creation

## Features

- Add new users with unique usernames  
- Securely hash passwords using bcrypt  
- View users (passwords are hidden)  
- Timestamp user creation  

## Setup

1. Clone this repository:
```bash
git clone https://github.com/mfliexx/secure-users-db.git
cd secure-users-db

2. Create a .env file and add your database credentials:
DB_NAME=postgres
DB_USER=postgres
DB_PASS=your_password


3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python user_management.py
