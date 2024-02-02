"""
    This is the main file for the bot.
"""

import logging
import asyncio
import json
import discord
from discord.ext import commands
from database.crud import Database
from helpers.files.load_commands import loadCommands
from helpers.logs import Logger

# Load secrets from secrets.json
with open("secrets.json", encoding="utf-8") as secrets_file:
    secrets = json.load(secrets_file)

# Set up the logger
startup_logging = logging.getLogger("discord.bot.startup")

# Create a new bot instance
bot = commands.Bot(
    command_prefix=secrets["prefix"],
    intents=discord.Intents.all(),
    description=secrets["description"],
    owner_id=secrets["owner_id"],
    case_insensitive=True,
)


@bot.event
async def on_ready():  # pylint: disable=invalid-name
    """
    Event: Bot is ready

    This event is called when the bot is ready to be used and prints information about the bot.
    """

    if bot.user is not None:
        startup_logging.info("Logged in as %s", bot.user.name)

        # Print the join URL
        startup_logging.info(
            "Invite URL: \
https://discord.com/api/oauth2/authorize?client_id=%s&permissions=8&scope=bot",
            bot.user.id,
        )

    # list all servers the bot is connected to
    if bot.user is not None:
        startup_logging.info(
            "%s is connected to %s guilds", bot.user.name, len(bot.guilds)
        )


def main():
    """
    Main entry point for the bot.
    """

    # Mention the startup da

    # Load the database
    Database.connect_to_database()

    # Set up overall logging
    Logger.setup_logging(secrets["log_level"])

    asyncio.run(loadCommands(bot, "commands"))

    # Run the bot

    # pylint: disable=no-value-for-parameter
    bot.run(
        secrets["discord_token"],
        reconnect=True,
    )


# Run the main function
if __name__ == "__main__":
    main()
