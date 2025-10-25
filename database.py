import sqlite3

def create_connection():
    conn = sqlite3.connect("hospital.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        gender TEXT,
                        diagnosis TEXT,
                        admission_date TEXT,
                        discharge_date TEXT
                    )''')
    conn.commit()
    conn.close()
