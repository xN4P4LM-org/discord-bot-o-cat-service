"""
This is the class that defines the permissions for the bot and is handled on a per guild basis.
"""

from helpers.database.delete import deleteFromTable
from helpers.database.create import createTable, insertIntoTable
from helpers.database.read import readTable


class Permissions:
    """
    This class is used to define the permissions for the bot and is handled on a per guild basis.
    """

    @staticmethod
    def check_if_table_exists( guild_id: int) -> None:
        """
        Check if the table exists in the database.
        """

        if not bool(readTable(f"permissions_{guild_id}")):
            createTable(f"permissions_{guild_id}", ["permission_name TEXT", "color TEXT"])

    @staticmethod
    def add_permission(guild_id:int, permission: str, color: str) -> None:
        """
        Set the permissions for the bot.
        """
        insertIntoTable(f"permissions_{guild_id}",
                        ["permission_name", "color"],
                        [permission, color])


    @staticmethod
    def get_all_permission_names(guild_id:int):# -> list[str]:
        """
        Get the permissions for the bot.
        """
        #TODO


    @staticmethod
    def remove_permission(guild_id:int,  permission: str) -> None:
        """
        Remove a permission from the bot.
        """
        deleteFromTable(f"permissions_{guild_id}", ["permission_name"], [permission])

    @staticmethod
    def update_permissions(
            guild_id:int, 
            old_permission_name: str,
            new_permission_name: str,
            old_color: str | None = None,
            new_color: str | None = None
        ) -> None:
        """
        Update the permissions for the bot.
        """

        #TODO

    @staticmethod
    def update_color(guild_id:int, permission: str, color: str) -> None:
        """
        Update the color for the permission.
        """
        #TODO

    @staticmethod
    def get_permission_color(guild_id:int, permission: str):# -> str:
        """
        Get the color for the permission.
        """
        #TODO

    @staticmethod
    def get_all_permissions(guild_id:int):# -> dict[str,str]:
        """
        Get all the permissions for the bot.
        """
        #TODO

    @staticmethod
    def get_all_permissions_and_colors(guild_id:int):# -> dict[str,str]:
        """
        Get all the permissions and colors for the bot.
        """
        #TODO