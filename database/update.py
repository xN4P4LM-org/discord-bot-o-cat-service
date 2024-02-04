"""
This file contains the update operations for the database.
"""
import logging
from database.execute_operation import executeCommand

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

    db_result = executeCommand(db_command, "commit")

    if isinstance(db_result, bool):
        return db_result

    return False
