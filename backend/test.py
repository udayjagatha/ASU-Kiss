import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "database": "user_management",
    "user": "root",
    "password": "Puppy$7677",
    "port": 3306
}

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Connection successful!")
    conn.close()
except mysql.connector.Error as e:
    print(f"Connection failed: {e}")
