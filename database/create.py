"""
This file contains the create operations for the database.
"""
import logging
from sqlite3 import OperationalError
from database.connection import getDbConnection
from database.validation import stringValidation

logger = logging.getLogger("discord.db.create")

# Create a table
def createTable(table_name: str, fields: list[str]) -> bool:
    """
    Create a table in the database.

    Arguments:
        table_name: The name of the table to create.
        fields: The fields to create in the table.
    """

    valid_opeartion = stringValidation(table_name)

    if not valid_opeartion:
        logger.error("Table name %s is not valid", table_name)
        return False

    db_command = f"CREATE TABLE IF NOT EXISTS {table_name} ( "

    for field in fields:
        db_command += "\n".join(field) + ", "

    db_command = db_command[:-2] + ")"

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
