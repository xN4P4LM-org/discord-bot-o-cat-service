"""
This module contains the logging configuration for the discord bot.
"""

from abc import abstractmethod
import logging
import logging.handlers
import sys
from helpers.env import getEnvVar
from helpers.terminal_colors import TerminalColors

class CustomFormatter(logging.Formatter):
    """
    This class is used to create a custom logging formatter.
    """
    debugging_enabled = False

    # get debugging status from variables and cast to a bool
    log_level = getEnvVar("DISCORD_BOT_LOG_LEVEL")

    if log_level is not None:
        if log_level == 10:
            debugging_enabled = True

    if debugging_enabled is True:
        pre_format = "%(asctime)s: 	%(funcName)s:%(lineno)d | %(pathname)s	"

    if debugging_enabled is False:
        pre_format = "%(asctime)s: "

    level_format = "%(levelname)-8s"
    post_format = " | %(name)-35s | %(message)s"

    FORMATS = {
        logging.DEBUG: TerminalColors.BLUE,
        logging.INFO: TerminalColors.GREEN,
        logging.WARNING: TerminalColors.YELLOW,
        logging.ERROR: TerminalColors.RED,
        logging.CRITICAL: TerminalColors.RED,
    }

    def format(self, record: logging.LogRecord):
        """
        Initialize the formatter
        """

        # Set the date format
        dt_fmt = "%Y-%m-%d %H:%M:%S"

        # Set the log format
        color_code = self.FORMATS.get(
            record.levelno,
            TerminalColors.RESET_COLOR
        )
        log_fmt = (
            self.pre_format
            + color_code
            + self.level_format
            + TerminalColors.RESET_COLOR
            + self.post_format
        )

        # Create the formatter
        formatter = logging.Formatter(log_fmt, dt_fmt, style="%")

        # Return the formatted record
        return formatter.format(record)


class Logger:
    """
    This class is used to create a global logging instance for the bot.
    """

    log_level = logging.INFO

    def __init__(self, log_level: int):
        """
        Initialize the logger.
        """
        self.log_level = log_level

    @staticmethod
    def setup_logging(log_level: int):
        """
        Setup the logging configuration for the bot
        """
        logger = Logger(log_level)
        logger.setup_root_logging()
        logger.setup_discord_logging()
        logger.setup_db_logging()

    def setup_root_logging(self):
        """
        Setup the root logging configuration for the bot
        """
        # Create the root logger
        root_logger = logging.getLogger("root")

        # Set the log level for the root logger
        root_logger.setLevel(self.log_level)

        # Create the console handler
        console_handler = logging.StreamHandler(sys.stdout)

        # Attach the formatter to the console_handler
        console_handler.setFormatter(CustomFormatter())

        # Add the console_handler to the main bot logger
        root_logger.addHandler(console_handler)

    def setup_discord_logging(self):
        """
        Setup the logging configuration for the discord library
        """

        # create the logger for the discord module
        discord_logger = logging.getLogger("discord")

        # Set the log level for the discord logger
        discord_logger.setLevel(self.log_level)

        # Set the log level for the http logger
        logging.getLogger("discord.http").setLevel(logging.INFO)

    def setup_db_logging(self):
        """
        Setup the logging configuration for the database module
        """

        # Create the logger for the database module
        db_logger = logging.getLogger("discord.db")

        # Set the log level for the database logger
        db_logger.setLevel(self.log_level)

    @abstractmethod
    def setup_cog_logging(self):
        """
        Abstract method to setup the logging configuration for custom cog modules
        """
