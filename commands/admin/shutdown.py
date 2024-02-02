"""
This module contains the shutdown command for the bot.
"""

import logging
from discord.ext import commands

logger = logging.getLogger("discord.command.admin.shutdown")


@commands.command()
async def shutdown(ctx: commands.Context):
    """
    Command: shutdown

    This command is used to shutdown the bot.
    """
    if ctx.author.id != ctx.bot.owner_id:
        logger.warning("User %s tried to shutdown the bot.", ctx.author)
        await ctx.send("You are not allowed to use this command!")
        return
    logger.info("User %s is shutting down the bot.", ctx.author)
    await ctx.send("Shutting down...")
    await ctx.bot.close()


async def setup(bot: commands.Bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(shutdown)
