import sqlite3
from datetime import datetime

def add_transaction(type, category, amount):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
        (type, category, amount, date)
    )

    conn.commit()
    conn.close()


def view_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def get_balance():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0

    conn.close()

    return income - expense