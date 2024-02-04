"""
Class for the database configuration for the bot and all cogs.
"""

import sys
import logging
import sqlite3

def getDbConnection() -> sqlite3.Connection | None:
    """
    Connects and returns a cursor for the database.
    """
    conn = sqlite3.connect("db/database.db")

    if conn is not None:
        logging.getLogger("discord.db").info("Connected to the database")
        return conn

    if conn is None:
        logging.getLogger("discord.db").critical("Failed to connect to the database")
        sys.exit(1)

    return None
