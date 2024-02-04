"""
This file contains the update operations for the database.
"""
import logging
from sqlite3 import OperationalError
from database.connection import getDbConnection

logger = logging.getLogger("discord.db.update")


def updateTable(table_name: str, fields: list[str]) -> bool:
    """
    Update a table in the database.

    Arguments:
        table_name: The name of the table to update.
        fields: The fields to update in the table.
    """

    db_command = f"UPDATE {table_name} SET "

    for field in fields:
        db_command += "\n".join(field) + ", "

    db_command = db_command[:-2]

    conn = getDbConnection()

    cursor = conn.cursor()
    cursor.execute(db_command)
    try:
        conn.commit()
        return True
    except OperationalError as e:
        logger.critical(e)
        return False
    finally:
        cursor.close()
        conn.close()
