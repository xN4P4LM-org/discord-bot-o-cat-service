"""
    This is the main file for the bot.
"""

import logging
import discord
from discord.ext import commands
from database.connection import getDbConnection
from helpers.load_commands import loadCommands
from helpers.get_file import getFile
from helpers.logs import Logger
from helpers.env import getEnvVar
from helpers.terminal_colors import TerminalColors


def main():
    """
    Main entry point for the bot.
    """
    # Set up overall logging
    Logger.setup_logging(int(getEnvVar("DISCORD_BOT_LOG_LEVEL")))

    # Set up the logger
    startup_logging = logging.getLogger("discord.bot.startup")

    # Create a new bot instance
    bot = commands.Bot(
        command_prefix=getEnvVar("DISCORD_BOT_COMMAND_PREFIX"),
        intents=discord.Intents.all(),
        description=getEnvVar("DISCORD_BOT_DESCRIPTION"),
        owner_id=int(getEnvVar("DISCORD_BOT_OWNER_ID")),
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

        This event is called when the bot is ready to be used and 
        prints information about the bot.
        """

        if bot.user is not None:
            startup_logging.info("Logged in as %s", bot.user.name)

            # Print the join URL
            startup_logging.info(
                "Invite URL: \
%shttps://discord.com/api/oauth2/authorize?\
client_id=%s&permissions=8&scope=bot%s",
                TerminalColors.GREEN_BOLD,
                bot.user.id,
                TerminalColors.RESET_COLOR
            )

        # list all servers the bot is connected to
        if bot.user is not None:
            startup_logging.info(
                "%s%s%s is connected to %s%s guilds %s",
                TerminalColors.GREEN_BOLD,
                bot.user.name,
                TerminalColors.RESET_COLOR,
                TerminalColors.GREEN_BOLD,
                len(bot.guilds),
                TerminalColors.RESET_COLOR
            )

        startup_logging.info("Loading commands...")
        await loadCommands(bot, "commands")

    # Read public ssh key from file and log it
    startup_logging.info(
        "Public SSH key: %s%s%s",
        TerminalColors.GREEN_BOLD,
        getFile("/root/.ssh/id_ed25519.pub").strip("\n"),
        TerminalColors.RESET_COLOR
    )

    # Run the bot
    bot.run(
        getEnvVar("DISCORD_BOT_TOKEN"),
        log_handler=None,
    )


# Run the main function
if __name__ == "__main__":
    main()
