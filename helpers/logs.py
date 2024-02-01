"""
This module contains the logging configuration for the discord bot.
"""

from abc import abstractmethod
import logging
import logging.handlers


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
        logger.setup_command_logging()
        logger.setup_db_logging()

    def setup_root_logging(self):
        """
        Setup the root logging configuration for the bot
        """
        # Create the root logger
        root_logger = logging.getLogger("root")

        # Set the log level for the root logger
        root_logger.setLevel(self.log_level)

        # Create the rotating file handler
        handler = logging.handlers.RotatingFileHandler(
            filename="bot.log",
            encoding="utf-8",
            maxBytes=32 * 1024 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files
        )

        # set the date format
        dt_fmt = "%Y-%m-%d %H:%M:%S"

        # Create the formatter
        formatter = logging.Formatter(
            "[{asctime}] [{levelname}] - {name}: {message}", dt_fmt, style="{"
        )

        # Attach the formatter to the handler
        handler.setFormatter(formatter)

        # Add the handler to the main bot logger
        root_logger.addHandler(handler)

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

    def setup_command_logging(self):
        """
        Setup the logging configuration for the discord command module
        """

        # Create the logger for the discord command module
        command_logger = logging.getLogger("discord.command")

        # Set the log level for the command logger
        command_logger.setLevel(self.log_level)

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
