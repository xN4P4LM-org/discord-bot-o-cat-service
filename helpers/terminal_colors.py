"""
This file contains the static class to get terminal colors for use in the bot.
"""
class TerminalColors: # pylint: disable=too-few-public-methods
    """
    This class contains static methods to get terminal colors for use in the bot.
    """
    GREY = "\x1b[38;20m"
    GREY_BOLD = "\x1b[38;1m"
    GREEN = "\x1b[32;20m"
    GREEN_BOLD = "\x1b[32;1m"
    BLUE = "\x1b[34;20m"
    BLUE_BOLD = "\x1b[34;1m"
    YELLOW = "\x1b[33;20m"
    YELLOW_BOLD = "\x1b[33;1m"
    RED = "\x1b[31;20m"
    RED_BOLD = "\x1b[31;1m"
    WHITE = "\x1b[37;20m"
    WHITE_BOLD = "\x1b[37;1m"
    CYAN = "\x1b[36;20m"
    CYAN_BOLD = "\x1b[36;1m"
    MAGENTA = "\x1b[35;20m"
    MAGENTA_BOLD = "\x1b[35;1m"
    RESET_COLOR = "\x1b[0m"

# Define aliases for the color attributes
color = TerminalColors()
GREY = TerminalColors.GREY
GREY_BOLD = TerminalColors.GREY_BOLD
GREEN = TerminalColors.GREEN
GREEN_BOLD = TerminalColors.GREEN_BOLD
BLUE = TerminalColors.BLUE
BLUE_BOLD = TerminalColors.BLUE_BOLD
YELLOW = TerminalColors.YELLOW
YELLOW_BOLD = TerminalColors.YELLOW_BOLD
RED = TerminalColors.RED
RED_BOLD = TerminalColors.RED_BOLD
WHITE = TerminalColors.WHITE
WHITE_BOLD = TerminalColors.WHITE_BOLD
CYAN = TerminalColors.CYAN
CYAN_BOLD = TerminalColors.CYAN_BOLD
MAGENTA = TerminalColors.MAGENTA
MAGENTA_BOLD = TerminalColors.MAGENTA_BOLD
RESET_COLOR = TerminalColors.RESET_COLOR
