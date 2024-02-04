"""
    This is the main file for the bot.
"""

import logging
import json
import discord
from discord.ext import commands
from aiohttp import TraceConfig
from database.connection import Connection
from helpers.commands.load_commands import loadCommands
from helpers.logs import Logger


# Load secrets from secrets.json
with open("secrets.json", encoding="utf-8") as secrets_file:
    secrets = json.load(secrets_file)

# Set up overall logging
Logger.setup_logging(secrets["log_level"])

# Set up the logger
startup_logging = logging.getLogger("discord.bot.startup")


# Create async def on_request for aiohttp debugging
async def on_request_start(
    session, _trace_config_ctx, params
):  # pylint: disable=invalid-name
    """
    Event: Request start

    This event is called when a request is started.
    """
    logging.getLogger("discord.aiohttp.debugging").debug(
        "Starting request: %s - Using session %s", params.url, id(session)
    )


# Create async def on_request_end for aiohttp debugging
async def on_request_end(
    session, _trace_config_ctx, params
):  # pylint: disable=invalid-name
    """
    Event: Request end

    This event is called when a request is ended.
    """
    logging.getLogger("discord.aiohttp.debugging").debug(
        "Ending request: %s - Using session %s", params.url, id(session)
    )


# Set up the aiohttp trace config
trace_config = TraceConfig()
trace_config.on_request_start.append(on_request_start)
trace_config.on_request_end.append(on_request_end)

# Create a new bot instance
bot = commands.Bot(
    command_prefix=secrets["prefix"],
    intents=discord.Intents.all(),
    description=secrets["description"],
    owner_id=secrets["owner_id"],
    case_insensitive=True,
    http_trace=trace_config,
    enable_debug_events=True,
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

    startup_logging.info("Loading commands...")
    await loadCommands(bot, "commands")


def main():
    """
    Main entry point for the bot.
    """

    # Load the database
    db_connection = Connection.connect_to_database()

    # Run the bot
    bot.run(
        secrets["discord_token"],
        log_handler=None,
    )

    # Close the database connection
    Connection.close_database(db_connection)


# Run the main function
if __name__ == "__main__":
    main()
