"""
[add.py] - Add a role to the server.
"""

from discord.ext import commands
from commands.roles.generic import manipulateRoles


@commands.command()
async def addRoles(ctx, category):
    """
    Command: addRoles

    This command is used to add all roles from the provided category to the server.
    """
    await manipulateRoles(ctx, category, "add")


async def setup(bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(addRoles)
