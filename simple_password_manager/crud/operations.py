import sqlite3
from getpass import getpass

from crypto.crypto import encrypt_password, decrypt_password

DATABASE_NAME = 'keys.db'


def add_entry(master_password: str):
    """_summary_

    Args:
        master_password (str): _description_
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    service = input('Enter the service (e.g., Google, Facebook): ')
    username = input('Enter the username: ')
    raw_password = getpass('Enter the password: ')

    encrypted_password = encrypt_password(raw_password, master_password)

    cursor.execute('INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)', (service, username, encrypted_password))
    conn.commit()
    conn.close()

def update_entry(master_password: str):
    """_summary_

    Args:
        master_password (str): _description_
    """

def retrieve_entry(master_password: str):
    """_summary_

    Args:
        master_password (str): _description_
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    service = input("Enter the service: ")
    cursor.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    row = cursor.fetchone()

    if row:
        decrypted_password = decrypt_password(row[1], master_password)
        print(f"Username: {row[0]}, Password: {decrypted_password}")
    else:
        print("No entry found for the provided service.")
    conn.close()
