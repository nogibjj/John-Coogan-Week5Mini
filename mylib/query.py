"""Query the database"""

import sqlite3


def query( query ):
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(query)
    print("Top 5 rows of the GroceryDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


