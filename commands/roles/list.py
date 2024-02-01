"""
List of the possible roles for the server
"""

from discord.ext import commands
from commands.roles.generic import getRoleGroup, manipulateRoles


@commands.command()
async def listRoles(ctx, category):
    """
    Command: listRoles

    This command is used to list all roles in a provided category.
    """
    await manipulateRoles(ctx, category, "list")


@commands.command()
async def listMainRoles(ctx):
    """
    Command: listMainRoles

    This command is used to list all main role catagories.
    """
    main_roles = getRoleGroup("main")

    if main_roles is not None:
        for role in main_roles:
            await ctx.send(role)


@commands.command()
async def listOptionalRoles(ctx):
    """
    Command: listOptionalRoles

    This command is used to list all optional role catagories.
    """
    optional_roles = getRoleGroup("optional")

    if optional_roles is not None:
        for role in optional_roles:
            await ctx.send(role)


async def setup(bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(listRoles)
    bot.add_command(listMainRoles)
    bot.add_command(listOptionalRoles)
