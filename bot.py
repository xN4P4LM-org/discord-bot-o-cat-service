"""
    This is the main file for the bot.
"""
import logging
import logging.handlers
import traceback
import asyncio
import json
import os
import importlib

import discord
from discord.ext import commands
from database.crud import Database
from helpers.logs import Logger


async def loadCommands(bot):
    """
    Load all commands from the bot folder.
    """
    directory = "commands"
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".py") and not filename.startswith("__"):
                    module_name = f"{directory}.{folder}.{filename[:-3]}"
                    try:
                        module = importlib.import_module(module_name)
                        if hasattr(module, "setup"):
                            await module.setup(bot)
                            print(f"Loaded module {module_name}")
                    except ModuleNotFoundError:
                        print(f"Could not load module {module_name}")
                        traceback.print_exc()


def main():
    """
    Main entry point for the bot.
    """

    # Load the database
    Database.connect_to_database()

    # Load secrets from secrets.json
    with open("secrets.json", encoding="utf-8") as secrets_file:
        secrets = json.load(secrets_file)

    # Set up the logging configuration
    Logger.setup_logging(logging.INFO)

    # Create a new bot instance
    bot = commands.Bot(
        command_prefix=secrets["prefix"],
        intents=discord.Intents.all(),
        description=secrets["description"],
        owner_id=secrets["owner_id"],
    )

    @bot.event
    async def on_ready():  # pylint: disable=invalid-name
        """
        Event: Bot is ready

        This event is called when the bot is ready to be used and prints information about the bot.
        """
        if bot.user is not None:
            logging.info("Logged in as %s", bot.user.name)

            # Print the join URL
            logging.info(
                "Invite URL: \
                https://discord.com/api/oauth2/authorize?client_id=%s&permissions=8&scope=bot",
                bot.user.id,
            )

        # list all servers the bot is connected to
        logging.info("Bot is connected to the following guilds:")
        for guild in bot.guilds:
            logging.info("  - %s", guild.name)

    asyncio.run(loadCommands(bot))

    # Run the bot
    bot.run(
        secrets["discord_token"],
        log_handler=None,
        reconnect=True,
    )


# Run the main function
if __name__ == "__main__":
    main()
