"""
This file contains validation functions for database operations.
"""

import logging
logger = logging.getLogger("discord.db.validation")

def stringValidation(operation: str) -> bool:
    """
    Validate the operation is alphanumeric.

    Arguments:
        operation: The operation to validate.

    Returns:
        bool: True if the operation is valid, False otherwise.
    """

    # validate the string is just alphanumeric
    if not operation.isalnum():
        logger.error("Value %s is not alphanumeric", operation)
        return False

    return True

def numberValidation(operation: str) -> bool:
    """
    Validate the operation is a number.

    Arguments:
        operation: The operation to validate.

    Returns:
        bool: True if the operation is valid, False otherwise.
    """

    # validate the string is just alphanumeric
    if not operation.isnumeric():
        logger.error("Value %s is not a number", operation)
        return False

    return True
