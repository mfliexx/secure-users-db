import psycopg2
import bcrypt
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()


conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host="localhost",
    port=5432
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
""")

conn.commit()

def add_user(username, password):
     hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
     cur = conn.cursor()
     cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
     conn.commit()
     print("User added")
   

def view_users():
    cur = conn.cursor()
    cur.execute("SELECT id, username, created_at FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | Username: {row[1]} | Created at: {row[2]}")
    conn.commit()


def log_action(user_id, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

def main():
 while True:

    print("\n === MENU ===")
    print("1. Add user")
    print("2. Show all users")
    print("3. Exit")
    choice = input("Choose command: ").strip()

    if choice == "1":
        username = input("Enter username: ").strip()
        password = input("Enter password: ") #не знаю кстати нужно ли тут в начале int
        add_user(username, password)

    elif choice == "2":
        view_users()

    elif choice == "3":
        break

    else: 
        print("Wrong command. Try again")

if __name__ == "__main__":
    main()

    