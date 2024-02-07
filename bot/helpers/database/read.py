"""
This file contains the read operations for the database.
"""
import logging
from execute_operation import executeCommand

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

def readFromTable(table_name: str, fields: list[str], values: list[str]) -> list | bool:
    """
    Read values from a table in the database.

    Arguments:
        table_name: The name of the table to read values from.
        fields: The fields to read values from.
        values: The values to read from the fields.
    """

    db_command = f"SELECT * FROM {table_name} WHERE "

    for field, value in zip(fields, values):
        db_command += field + " = " + value + " AND "

    db_command = db_command[:-5]

    result = executeCommand(db_command, "fetchone")

    # if the type is not a list, then it is a boolean
    if isinstance(result, list):
        return result

    return False
