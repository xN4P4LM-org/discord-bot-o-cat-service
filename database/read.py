"""
This file contains the read operations for the database.
"""
import logging
from database.execute_operation import executeCommand

logger = logging.getLogger("discord.db.read")

def readTable(table_name: str) -> list | bool:
    """
    Read a table in the database.

    Arguments:
        table_name: The name of the table to read.
    """

    db_command = f"SELECT * FROM {table_name}"

    result = executeCommand(db_command, "fetchall")

    # if the type is not a list, then it is a boolean
    if isinstance(result, list):
        return result

    return False
