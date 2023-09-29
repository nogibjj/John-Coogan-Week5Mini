"""Query the database"""

import sqlite3


def query(query):
    """Dynamic query based off command line input"""
    conn = sqlite3.connect("GameDB.db")
    cursor = conn.cursor()
    cursor.execute(query)
    print(cursor.fetchall())
    conn.close()
    return "Success"
