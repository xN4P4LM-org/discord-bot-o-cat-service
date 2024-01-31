"""
List of the possible roles for the server
"""

from discord.ext import commands
from bot.roles.generic import manipulateRoles


@commands.command()
async def listRoles(ctx, category):
    """
    Command: listRoles

    This command is used to list all roles in a provided category.
    """
    await manipulateRoles(ctx, category, "list")


async def setup(bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(listRoles)
