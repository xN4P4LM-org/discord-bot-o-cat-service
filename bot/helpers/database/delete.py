"""
This file contains the delete operations for the database.
"""
import logging

from execute_operation import executeCommand
from validation import stringValidation

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

def deleteFromTable(table_name: str, fields: list[str], values: list[str]) -> bool:
    """
    Delete values from a table in the database.

    Arguments:
        table_name: The name of the table to delete values from.
        fields: The fields to delete values from.
        values: The values to delete from the fields.
    """
    valid_opeartion = stringValidation(table_name)

    if not valid_opeartion:
        logger.error("Table name %s is not valid", table_name)
        return False

    db_command = f"DELETE FROM {table_name} WHERE "

    for field, value in zip(fields, values):
        db_command += field + " = " + value + " AND "

    db_command = db_command[:-5]

    db_result = executeCommand(db_command, "commit")

    if isinstance(db_result, bool):
        return db_result

    return False
