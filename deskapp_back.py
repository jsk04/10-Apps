import sqlite3, sys

def main():
    pass

class Database:

    def __init__(self, db):
        """Create connection, and then create table."""
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert_data(self, title, author, year, isbn):
        """Insert the data that was passed in into the databse."""
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def search_data(self, title="", author="", year="", isbn=""):
        """Filter based on the parameters and display data from the database"""
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()

        return rows

    def delete_data(self, id):
        """Delete data in the database based on the ID passed in."""
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update_data(self, id, title, author, year, isbn):
        """Update selected data from the database with the parameters that are passed in."""
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def view_data(self):
        """Fetch all the data in the database to be displayed."""
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows

    def __del__(self):
        """Close connection to the database."""
        self.conn.close()

if __name__ == '__main__':
    main()