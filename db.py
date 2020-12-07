import sqlite3


class Database:
    # constructor
    def __init__(self, db):
        self.conn = sqlite3.connect(db)  # connexion
        self.cur = self.conn.cursor()  # executing query
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO ")
