"""
Class for the database configuration for the bot and all cogs.
"""

import logging
import sqlite3


class Connection:
    """
    This class contains the database configuration for the bot and all cogs.
    """

    @staticmethod
    def connect_to_database() -> bool:
        """
        Connect to the sqlite database.
        """

        conn = Connection.get_conn()

        if conn is not None:
            logging.getLogger("discord.db").info("Connected to the database")
            Connection.close_database(conn)
            return True

        if conn is None:
            logging.getLogger("discord.db").error("Failed to connect to the database")
            Connection.close_database(conn)
            return False

        return False


    @staticmethod
    def close_database(conn: sqlite3.Connection) -> None:
        """
        Close the connection to the sqlite database.
        """
        conn.close()

        logging.getLogger("discord.db").info("Closed the database connection")

    @staticmethod
    def get_conn() -> sqlite3.Connection:
        """
        Connects and returns a cursor for the database.
        """
        conn = sqlite3.connect("database.db")

        return conn
