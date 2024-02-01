"""
Initializing logging for the cog
"""

import logging
from helpers.logs import Logger


class CogLogger(Logger):
    """
    This class is used to create a logging instance for a cog
    by inheriting from the global logging class.
    """

    def setup_cog_logging(self):
        """
        Setup the logging configuration for the cog
        """
        # Create the cog logger
        cog_logger = logging.getLogger("cog")

        # Set the log level for the cog logger
        cog_logger.setLevel(self.log_level)
