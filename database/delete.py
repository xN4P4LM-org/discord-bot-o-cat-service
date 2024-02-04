"""
This file contains the delete operations for the database.
"""
import logging

from database.execute_operation import executeCommand
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

    db_result = executeCommand(db_command, "commit")

    if isinstance(db_result, bool):
        return db_result

    return False
