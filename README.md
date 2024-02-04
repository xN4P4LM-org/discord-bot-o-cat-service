# bot-o-cat

### ( This is a work in progress - use at your own risk )

## Overview

This is a general purpose bot that is designed to be customizable and extensible. It's built on top of the [discord.py](github.com/Rapptz/discord.py) library by [Rapptz](github.com/Rapptz).

## Features

## Running the bot

There are a few ways to run this bot, but the easiest way is to use Docker Compose.

### Standalone from source
```bash
pip install -r requirements.txt
python bot.py
```

### Docker Compose from source
```yaml
version: "3"
services:
  bot:
    container_name: discord-bot
    build:
      context: .
      dockerfile: dockerfile
    environment:
      - DISCORD_BOT_DESCRIPTION="A simple discord bot" 
      - DISCORD_BOT_TOKEN=  # Your bot token with no-quotes
      - DISCORD_BOT_OWNER_ID=
      - DISCORD_BOT_COMMAND_PREFIX=.
      - DISCORD_BOT_LOG_LEVEL=20 # 10=DEBUG, 20=INFO, 30=WARNING, 40=ERROR, 50=CRITICAL

    volumes:
      - discord:/app

volumes:
  discord:
```

## Required environment variables

- `DISCORD_BOT_DESCRIPTION` - The description of the bot
- `DISCORD_BOT_TOKEN` - Discord Token for your bot from the Discord Developer Portal
- `DISCORD_BOT_OWNER_ID` - The Bot Owner's user id
- `DISCORD_BOT_COMMAND_PREFIX` - Command Prefix Ex. `!`
- `DISCORD_BOT_LOG_LEVEL` - the int log level `(10, 20, 30, 40, 50)`
