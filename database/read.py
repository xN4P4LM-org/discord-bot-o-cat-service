"""
This file contains the read operations for the database.
"""
import logging
from sqlite3 import OperationalError
from database.connection import getDbConnection

logger = logging.getLogger("discord.db.read")

def readTable(table_name: str) -> list | bool:
    """
    Read a table in the database.

    Arguments:
        table_name: The name of the table to read.
    """

    db_command = f"SELECT * FROM {table_name}"

    conn = getDbConnection()

    cursor = conn.cursor()
    cursor.execute(db_command)
    try:
        rows = cursor.fetchall()
        return rows
    except OperationalError as e:
        logger.critical(e)
        return False
    finally:
        cursor.close()
        conn.close()
