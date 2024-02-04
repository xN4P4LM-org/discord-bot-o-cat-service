"""
This contains operations to read environment variables and return them to the caller.
"""

import os
import logging

logger = logging.getLogger("discord.env")

def getEnvVar(var_name: str) -> str | None:
    """
    Get an environment variable.

    Arguments:
        var_name: The name of the environment variable to get.

    Returns:
        str | bool: The value of the environment variable if it exists, False otherwise.
    """
    try:
        return os.environ[var_name]
    except KeyError as e:
        logger.error(e)
