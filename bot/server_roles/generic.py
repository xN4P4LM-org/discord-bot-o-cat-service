"""
This file contains generic functions that are used by the server_roles cog.
"""
from json_helpers.read_json import readJson


def checkIfRoleExists(role_name, ctx) -> bool:
    """
    This function checks if a role exists in the current server.
    """
    current_roles = ctx.guild.roles

    if any(existing_role.name == role_name for existing_role in current_roles):
        ctx.send(f"Role {role_name} already exists!")
        return True

    return False


def getRoleCategory(category) -> dict | None:
    """
    This function returns the role category from the provided category.
    """
    main_roles = readJson("roles/discord/main")
    optional_roles = readJson("roles/discord/optional")

    if category in main_roles:
        return main_roles[category]

    if category in optional_roles:
        return optional_roles[category]

    return None


async def manipulateRoles(ctx, category, action):
    """
    This function goes through all the roles and checks if the role exists.
    """
    action_name = None

    roles = getRoleCategory(category)

    if roles is not None:
        for role in roles["roles"]:
            role_name = role["name"]
            if not checkIfRoleExists(role_name, ctx):
                if action == "add":
                    action_name = "Added"
                    await ctx.guild.create_role(name=role_name)
                    await ctx.send(f"Added role {role_name} to the server!")
                elif action == "update":
                    action_name = "Updated"
                    # TODO: Update role
                    await ctx.send(f"Updated role {role_name}!")
                elif list == "list":
                    await ctx.send(role_name)
                else:
                    await ctx.send(f"Action {action} is not supported!")
        if action_name is not None:
            await ctx.send(f"{action_name} role category {category}!")

    else:
        await ctx.send(f"Role category {category} does not exist!")
