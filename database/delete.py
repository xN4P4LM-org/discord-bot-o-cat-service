"""
This file contains the delete operations for the database.
"""
import logging
from sqlite3 import OperationalError

from database.connection import Connection
from database.validation import stringValidation

logger = logging.getLogger("discord.db.delete")

def deleteTable(table_name: str) -> bool:
    """
    Delete a table in the database.

    Arguments:
        table_name: The name of the table to delete.
    """
    valid_opeartion = stringValidation(table_name)

    if not valid_opeartion:
        logger.error("Table name %s is not valid", table_name)
        return False

    db_command = f"DROP TABLE IF EXISTS {table_name}"

    conn = Connection.get_conn()

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
