"""
Class for the database configuration for the bot and all cogs.
"""

import logging
import sqlite3
from database.crud import CRUD


class Connection:
    """
    This class contains the database configuration for the bot and all cogs.
    """

    def __init__(self, conn) -> None:
        self.conn = conn
        self.crud = CRUD(conn)

        self.logger = logging.getLogger("discord.db")

    @staticmethod
    def connect_to_database():
        """
        Connect to the sqlite database.
        """
        conn = sqlite3.connect("database.db")
        Connection(conn)

        if conn is not None:
            logging.getLogger("discord.db").info("Connected to the database")

        if conn is None:
            logging.getLogger("discord.db").error("Failed to connect to the database")

        return conn

    @staticmethod
    def close_database(conn: sqlite3.Connection):
        """
        Close the connection to the sqlite database.
        """
        conn.close()

        logging.getLogger("discord.db").info("Closed the database connection")

    async def get_conn(self):
        """
        Return the cursor for the database.
        """
        return self.conn
