"""
    This is the main file for the bot.
"""

import logging
import discord
from discord.ext import commands
from database.connection import getDbConnection
from helpers.commands.load_commands import loadCommands
from helpers.logs import Logger
from helpers.env import getEnvVar


def main():
    """
    Main entry point for the bot.
    """

    # get log_level from environment variables
    log_level = getEnvVar("DISCORD_BOT_LOG_LEVEL")

    if log_level is None:
        # default to 20 (INFO) if no log level is set
        log_level = 20

    # Set up overall logging
    Logger.setup_logging(int(log_level))

    # Set up the logger
    startup_logging = logging.getLogger("discord.bot.startup")

    # get command prefix from environment variables
    command_prefix = getEnvVar("DISCORD_BOT_COMMAND_PREFIX")

    if command_prefix is None:
        startup_logging.critical("No command prefix found. Exiting...")
        return

    # get owner id from environment variables
    owner_id = getEnvVar("DISCORD_BOT_OWNER_ID")

    if owner_id is None:
        startup_logging.critical("No owner id found. Exiting...")
        return

    # get description from environment variables
    description = getEnvVar("DISCORD_BOT_DESCRIPTION")

    if description is None:
        startup_logging.critical("No description found. Exiting...")
        return

    # Create a new bot instance
    bot = commands.Bot(
        command_prefix=command_prefix,
        intents=discord.Intents.all(),
        description=description,
        owner_id=int(owner_id),
        case_insensitive=True,
    )

    # Test the database connection
    db_conn = getDbConnection()

    if db_conn is not None:
        db_conn.close()

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

        startup_logging.info("Loading commands...")
        await loadCommands(bot, "commands")

    discord_token = getEnvVar("DISCORD_BOT_TOKEN")

    if discord_token is None:
        startup_logging.critical("No Discord token found. Exiting...")
        return

    # Run the bot
    bot.run(
        discord_token,
        log_handler=None,
    )


# Run the main function
if __name__ == "__main__":
    main()
