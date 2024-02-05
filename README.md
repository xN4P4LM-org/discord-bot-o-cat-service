# Bot-O-Cat

[![Linting](https://github.com/xN4P4LM-org/bot-o-cat/actions/workflows/lint.yaml/badge.svg)](https://github.com/xN4P4LM-org/bot-o-cat/actions/workflows/lint.yaml)

### ( This is a work in progress - use at your own risk )

## Overview

This is a general purpose bot that is designed to be customizable and extensible. It's built on top of the [discord.py](https://github.com/Rapptz/discord.py) library by [Rapptz](https://github.com/Rapptz).

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
      - DISCORD_BOT_TOKEN= # Your bot token with no-quotes
      - DISCORD_BOT_OWNER_ID=
      - DISCORD_BOT_COMMAND_PREFIX=.
      - DISCORD_BOT_LOG_LEVEL=20 # 10=DEBUG, 20=INFO, 30=WARNING, 40=ERROR, 50=CRITICAL
    volumes:
      - discord_cogs:/bot/cogs
      - discord_db:/bot/db
      - git_ssh:/root/.ssh
      - discord_roles:/bot/roles

volumes:
  discord_cogs:
  discord_db:
  git_ssh:
  discord_roles:
```

## Required environment variables

- `DISCORD_BOT_DESCRIPTION` - The description of the bot
- `DISCORD_BOT_TOKEN` - Discord Token for your bot from the Discord Developer Portal
- `DISCORD_BOT_OWNER_ID` - The Bot Owner's user id
- `DISCORD_BOT_COMMAND_PREFIX` - Command Prefix Ex. `!`
- `DISCORD_BOT_LOG_LEVEL` - the int log level `(10, 20, 30, 40, 50)`

# Contributing

Please fork this repository and contribute back using [pull requests](https://github.com/xn4p4lm-org/bot-o-cat/pulls).
Ensure that when submitting code that you have read the [developer-certificate-of-origin](developer-certificate-of-origin) and that you have signed off on your commits with `git commit -s` or `git commit --signoff`.

Features request can be submitted by using [GitHub Issues](https://github.com/xn4p4lm-org/bot-o-cat/issues).

All code, comments, and critiques are greatly appreciated.

# License

bot-o-cat is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
