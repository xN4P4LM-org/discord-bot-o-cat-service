"""
This file is for handling the loading of commands
"""

import os
import importlib
import logging
import traceback

logger = logging.getLogger("discord.command.loader")


async def iterateCommands(bot, filename, directory, folder) -> None:
    """
    Load all commands from the bot folder.
    """
    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = f"{directory}.{folder}.{filename[:-3]}"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "setup"):
                await module.setup(bot)
                logger.info("Loaded module %s", module_name)
        except ModuleNotFoundError:
            logger.warning("Could not load module %s", module_name)
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
