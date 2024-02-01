"""
Update the server roles.
"""

from discord.ext import commands
from commands.roles.generic import manipulateRoles


@commands.command()
async def updateRoles(ctx, category):
    """
    Command: updateRoles

    This command is used to update all roles in a provided category.
    """
    await manipulateRoles(ctx, category, "update")


async def setup(bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(updateRoles)
