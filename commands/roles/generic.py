"""
This file contains generic functions that are used by the server_roles cog.
"""

import os
import json
from typing import Any


def checkIfRoleExists(role_name, ctx) -> bool:
    """
    This function checks if a role exists in the current server.
    """
    current_roles = ctx.guild.roles

    if any(existing_role.name == role_name for existing_role in current_roles):
        ctx.send(f"Role {role_name} already exists!")
        return True

    return False


def getRoleGroup(group: str) -> dict | None:
    """
    This function returns the role category from the provided category.
    """

    role_directories = getAllRoles()

    list_of_roles = dict[str, dict[Any, Any]]()

    if group not in role_directories:
        return None

    for role_directory in role_directories:
        for _, _, role_file in os.walk(role_directory):
            for role in role_file:
                if role.endswith(".json"):
                    with open(
                        f"{role_directory}/{role}", encoding="utf-8"
                    ) as role_file:
                        role_data = json.load(role_file)
                        list_of_roles[role] = role_data

    return list_of_roles


def getRoleCategory(category: str) -> dict | None:
    """
    This function returns the role category from the provided category.
    """

    role_directories = getAllRoles()

    for role_directory in role_directories:
        for _, _, role_file in os.walk(role_directory):
            for role in role_file:
                if role == f"{category}.json":
                    with open(
                        f"{role_directory}/{role}", encoding="utf-8"
                    ) as role_file:
                        return json.load(role_file)

    return None


def getAllRoles() -> list:
    """
    This function returns all the roles.
    """

    # walk the /roles/discord directory and get all folders
    # and append the directory name to the list
    role_categories = []

    for found_dirs, _, _ in os.walk("roles/discord"):
        if found_dirs != "roles/discord":
            role_categories.append(found_dirs)

    return role_categories


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

                    await ctx.send("Not Implemented!")
                elif list == "list":
                    await ctx.send(role_name)
                else:
                    await ctx.send(f"Action {action} is not supported!")
        if action_name is not None:
            await ctx.send(f"{action_name} role category {category}!")

    else:
        await ctx.send(f"Role category {category} does not exist!")
