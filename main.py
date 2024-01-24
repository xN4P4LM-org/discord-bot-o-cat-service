"""
    This is the main file for the bot.
"""
import traceback
import asyncio
import sqlite3
import json
import os
import importlib
import discord
from discord.ext import commands

from json_helpers.read_json import readJson
from database.crud import loadDatabase


async def loadCommands(bot):
    """
    Load all commands from the bot folder.
    """
    directory = "bot"
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

    # Connect to the database
    conn = sqlite3.connect("database.db")

    # Load the database
    loadDatabase(conn)

    # Load secrets from secrets.json
    with open("secrets.json", encoding="utf-8") as secrets_file:
        secrets = json.load(secrets_file)

    main_roles = readJson("roles/discord/main")
    optional_roles = readJson("roles/discord/optional")
    # bot_roles = readJson("roles/bot/bot.json")

    # Create a new bot instance
    bot = commands.Bot(
        command_prefix=secrets["prefix"],
        intents=discord.Intents.all(),
        description=secrets["description"],
    )

    @bot.event
    async def on_ready():  # pylint: disable=invalid-name
        """
        Event: Bot is ready

        This event is called when the bot is ready to be used and prints information about the bot.
        """
        if bot.user is not None:
            print(f"Logged in as {bot.user.name}")

            # Print the join URL
            print(
                f"Invite URL: \
                https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
            )

        # list all servers the bot is connected to
        print("Connected to:")
        for guild in bot.guilds:
            print(f"- {guild.name}")

    @bot.command()
    async def shutdown(ctx):
        """
        Command: shutdown

        This command is used to shutdown the bot.
        """
        if ctx.author.id != secrets["owner_id"]:
            await ctx.send("You are not allowed to use this command!")
            return
        await ctx.send("Shutting down...")
        await bot.close()

    @bot.command()
    async def listMainRoles(ctx):
        """
        Command: listMainRoles

        This command is used to list all main role catagories.
        """
        for role in main_roles:
            await ctx.send(role)

    @bot.command()
    async def listOptionalRoles(ctx):
        """
        Command: listOptionalRoles

        This command is used to list all optional role catagories.
        """
        for role in optional_roles:
            await ctx.send(role)

    asyncio.run(loadCommands(bot))

    # Run the bot
    bot.run(secrets["discord_token"])


# Run the main function
if __name__ == "__main__":
    main()
