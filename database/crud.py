"""
This module contains the CRUD class which is used to 
create, read, update and delete records from the database.
"""

import logging
from sqlite3 import DatabaseError, OperationalError


class CRUD:
    """
    This class contains the CRUD methods for the sqlite database.
    """

    def __init__(self, conn) -> None:
        self.conn = conn

        self.logger = logging.getLogger("discord.db")

    @staticmethod
    def load_database(conn):
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

    # Create a table
    def create_table(self):
        """
        Create a table in the database.
        """
        cursor = self.conn.cursor()
        cursor.execute(
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
    def insert_record(self, name, age) -> None | OperationalError:
        """
        insert a record into the database.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (name, age)
            VALUES (?, ?)
        """,
            (name, age),
        )
        self.conn.commit()

    # Read all records
    def read_all_records(self) -> list | DatabaseError:
        """
        read all records from the database.
        """

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM users")

        if cursor.rowcount == 0:
            error = DatabaseError("No records found")
            self.logger.critical(error)
            return error

        return cursor.fetchall()

    # Update a record
    def update_record(self, record_id, name, age) -> None | OperationalError:
        """
        update a record in the database.
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET name = ?, age = ?
            WHERE id = ?
        """,
            (name, age, record_id),
        )

        if cursor.rowcount == 0:
            error = OperationalError("Record not found")
            self.logger.critical(error)
            return error

        self.conn.commit()

    # Delete a record
    def delete_record(self, database, record_id) -> None | DatabaseError:
        """
        delete a record from the database.
        """
        cursor = self.conn.cursor()

        cursor.execute(f"DELETE FROM {database} WHERE id = {record_id}")

        if cursor.rowcount == 0:
            error = DatabaseError("Record not found")
            self.logger.critical(error)
            return error

        self.conn.commit()
