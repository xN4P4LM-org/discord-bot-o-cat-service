"""
This file is for handling the loading of commands
"""

import os
import importlib
import logging
import traceback
from helpers.logs import TerminalColors


async def iterateCommands(bot, filename, directory, folder) -> None:
    """
    Load all commands from the bot folder.
    """
    logger = logging.getLogger("discord.command.loader")

    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = f"{directory}.{folder}.{filename[:-3]}"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "setup"):
                await module.setup(bot)
                logger.info("Loaded module %s%s%s",
                            TerminalColors.GREEN_BOLD,
                            module_name,
                            TerminalColors.RESET_COLOR)
        except ModuleNotFoundError:
            logger.warning("Could not load module %s%s%s",
                            TerminalColors.RED_BOLD,
                            module_name,
                            TerminalColors.RESET_COLOR)
            logger.warning(traceback.format_exc())


async def loadCommands(bot, directory) -> None:
    """
    Iterate through the commands folder and load all commands.
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                await iterateCommands(bot, filename, directory, folder)
