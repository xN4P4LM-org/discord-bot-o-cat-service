"""
This module contains the CRUD class which is used to 
create, read, update and delete records from the database.
"""


def loadDatabase(conn):
    """
    Load the database from the database.db file.
    """
    # check if the users table exists
    cursor = conn.cursor()
    cursor.execute(
        "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users'"
    )
    if cursor.fetchone()[0] == 1:
        print("Table exists")
    else:
        print("Table does not exist")
        cursor.execute("CREATE TABLE users (id int, name text, roles text)")
        conn.commit()


class CRUD:
    """
    This class contains the CRUD methods for the sqlite database.
    """

    def __init__(self, conn, cursor) -> None:
        self.conn = conn
        self.cursor = cursor

    # Create a table
    def create_table(self):
        """
        Create a table in the database.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        """
        )
        self.conn.commit()

    # Insert a record
    def insert_record(self, name, age):
        """
        insert a record into the database.
        """
        self.cursor.execute(
            """
            INSERT INTO users (name, age)
            VALUES (?, ?)
        """,
            (name, age),
        )
        self.conn.commit()

    # Read all records
    def read_all_records(self):
        """
        read all records from the database.
        """
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    # Update a record
    def update_record(self, record_id, name, age):
        """
        update a record in the database.
        """
        self.cursor.execute(
            """
            UPDATE users
            SET name = ?, age = ?
            WHERE id = ?
        """,
            (name, age, record_id),
        )
        self.conn.commit()

    # Delete a record
    def delete_record(self, database, record_id):
        """
        delete a record from the database.
        """
        self.cursor.execute(f"DELETE FROM {database} WHERE id = {record_id}")
        self.conn.commit()
