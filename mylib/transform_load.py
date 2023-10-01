"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="../sqlite-lab_John-Coogan/data/game_data.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(
        open(dataset, newline="", encoding="iso-8859-1"), delimiter=","
    )
    conn = sqlite3.connect("GameDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS GameDB")
    c.execute(
        "CREATE TABLE GameDB (Rank,Name, Platform, Publisher, Developer, Critic_Score, User_Score, Total_Shipped, Year)"
    )
    # insert
    c.executemany("INSERT INTO GameDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "GameDB.db"
