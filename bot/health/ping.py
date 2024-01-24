"""
This file contains the ping command for a health check.
"""
from discord.ext import commands


# command: Ping
@commands.command()
async def ping(ctx):
    """
    Command: ping

    This command is used to test if the bot is running or frozen.
    """
    await ctx.send("Pong!")


# Command: Ping
@commands.command()
async def messagePing(ctx, message):
    """
    Command: messagePing

    This command is like ping but with a message.
    """
    await ctx.send(f"Pong! - {message}")


async def setup(bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(ping)
    bot.add_command(messagePing)
