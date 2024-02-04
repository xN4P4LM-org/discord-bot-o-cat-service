"""
This file will get a corrisponding file and return it to the caller.
"""

import logging
import sys

logger = logging.getLogger("discord.file_handler")

def getFile(file_name: str) -> str:
    """
    Get a file from the file system.

    Arguments:
        file_name: The name of the file to get.

    Returns:
        str | bool: The contents of the file if it exists, False otherwise.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            logger.info("File %s read successfully", file_name)
            return file.read()
    except FileNotFoundError as e:
        logger.error("File %s not found: %s", file_name, e)
        sys.exit(1)
    except FileExistsError as e:
        logger.error("Failed to read file %s: %s", file_name, e)
        sys.exit(1)
