import os
import sqlite3


DATABASE_NAME = 'keys.db'


def initialize_db():
    """Initialize database"""
    if not os.path.exists(DATABASE_NAME):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL)
            ''')
        cursor.execute('''
            CREATE TABLE notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT
                title TEXT NOT NULL,
                body TEXT NOT NULL)
            ''')
        conn.commit()
        conn.close()
