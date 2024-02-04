"""
This is a simple example of a cog that listens for events and has a command.
"""
import discord
from discord.ext import commands


class Greetings(commands.Cog, name="Hello"):
    """
    This class contains the greetings cog for the bot.
    """

    def __init__(self, bot):
        """
        Initialize the cog.
        """
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Event: on_member_join

        This event is called when a member joins the server.
        """
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}.")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member | None = None):
        """
        Command: hello

        This command is used to greet a member.
        """
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}~")
        else:
            await ctx.send(f"Hello {member.name}... This feels familiar.")
        self._last_member = member
