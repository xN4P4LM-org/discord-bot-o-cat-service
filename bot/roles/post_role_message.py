"""
This is used to create a rich embed message for the server roles,
where you can react to the message to get the role.
"""
from string import ascii_lowercase as letters
from discord.ext import commands
from discord import Embed, Color
from bot.roles.generic import getRoleCategory


async def postEmojiEmbed(ctx, category_result, roles, channel_id, emoji_type):
    """ "
    This function posts a rich embed message with the roles provided
    and adds reactions either with a-z (Letters) or 1-9 (Numbers).
    """
    emoji = []

    numbers_to_emoji = {
        1: ":one:",
        2: ":two:",
        3: ":three:",
        4: ":four:",
        5: ":five:",
        6: ":six:",
        7: ":seven:",
        8: ":eight:",
        9: ":nine:",
    }

    # Letter structure is :regional_indicator_a: - :regional_indicator_z:
    # Number structure is :one: - :nine:

    if emoji_type == "letters":
        for letter in letters:
            emoji.append(f":regional_indicator_{letter}:")

    if emoji_type == "numbers":
        for number in range(1, 10):
            emoji.append(numbers_to_emoji[number])

    embed = Embed(
        title=category_result["title"],
        description=category_result["description"],
        color=Color.dark_embed(),
    )
    role_emoji = emoji.copy()
    for role in roles:
        embed.add_field(
            value=f"{role_emoji.pop(0)} for {role['name']}",
            name="",
            inline=False,
        )


@commands.command()
async def postRoleMessage(ctx, category, channel_id=None):
    """
    Command: postRoleMessage

    This command is used to post a message with all the roles in a provided category.
    """
    if channel_id is None:
        channel_id = ctx.channel.id

    category_result = getRoleCategory(category)
    roles = category_result.get("roles") if category_result is not None else []

    if isinstance(roles, list):
        if len(roles) == 0:
            await ctx.send(f"No roles found for category {category}!")
        elif len(roles) >= 9:
            await postEmojiEmbed(ctx, category_result, roles, channel_id, "numbers")
        else:
            array_of_roles = []
            chunk_size = 26
            for i in range(0, len(roles), chunk_size):
                array_of_roles.append(roles[i : i + chunk_size])

            for roles in array_of_roles:
                await postEmojiEmbed(ctx, category_result, roles, channel_id, "letters")


async def setup(bot):
    """
    Add the commands to the bot.
    """
    bot.add_command(postRoleMessage)
