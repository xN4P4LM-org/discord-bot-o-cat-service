"""
This file contains the reusable code to execute the operations
on the database.
"""
import logging
from sqlite3 import OperationalError
from typing import Any
from connection import getDbConnection

logger = logging.getLogger("discord.db.execute")

# Execute a command
def executeCommand(command: str, operations:str) -> bool | list[Any] | Any:
    """
    Execute a command on the database.

    Arguments:
        command: The command to execute on the database.
        operations: The type of operation to perform.

    Returns:
        bool or list or Any: The result of the operation.
    """
    conn = getDbConnection()

    cursor = conn.cursor()
    cursor.execute(command)
    logger.debug("Executing command: %s", command)
    try:
        if operations == "commit":
            conn.commit()
            return True
        if operations == "fetchall":
            result = cursor.fetchall()
            return result
        if operations == "fetchone":
            result = cursor.fetchone()
            return result
    except OperationalError as e:
        logger.critical(e)
        logger.error("Command %s failed", command)
    finally:
        cursor.close()
        conn.close()

    return False
