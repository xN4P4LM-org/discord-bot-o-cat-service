# Bot-O-Cat

[![Linting](https://github.com/xN4P4LM-org/bot-o-cat/actions/workflows/lint.yaml/badge.svg)](https://github.com/xN4P4LM-org/bot-o-cat/actions/workflows/lint.yaml)

### ( This is a work in progress - use at your own risk )

## Overview

This is a general purpose bot where the primary intention is to enable server owners, as well as third parties to create a bot that is tailored to their specific need or uses cases. The bot is designed to be modular. You can add new features and functionality without the need to modify the core codebase or you can create your own bot using this as a framework.

## Features

This is the main project, the core functionality is divided into git submodules:

- [bot](https://github.com/xN4P4LM-org/bot-o-cat_bot) - The discord bot portion of the project using [Python3](https:// and [discord.py](https://github.com/Rapptz/discord.py).
- [api](https://github.com/xN4P4LM-org/bot-o-cat_api) - The API portion of the project using Golang and the [Gin](https://github.com/gin-gonic/gin) framework.
- [web](https://github.com/xN4P4LM-org/bot-o-cat_web) - The web portion of the project, it is currently not implemented.

## Running the bot

To run this bot you will use the following `docker-compose` file and a docker compatible environment.

```yaml
version: "3"
services:
  bot:
    container_name: discord-bot
    build: ./bot
    environment:
      - DISCORD_BOT_DESCRIPTION="A simple discord bot"
      - DISCORD_BOT_TOKEN=
      - DISCORD_BOT_OWNER_ID=
      - DISCORD_BOT_COMMAND_PREFIX=.
      - DISCORD_BOT_LOG_LEVEL=20 # 10=DEBUG, 20=INFO, 30=WARNING, 40=ERROR, 50=CRITICAL
      - DISCORD_MONGO_DB_HOST_NAME=mongo-db
      - DISCORD_MONGO_DB_PORT=27017
    volumes:
      - discord_cogs:/bot/cogs
      - discord_git_ssh:/root/.ssh
    depends_on:
      mongo-db:
        condition: service_healthy
        restart: true

  mongo-db:
    container_name: discord-mongodb
    build: ./db
    environment:
      - MONGO_INITDB_ROOT_USERNAME=
      - MONGO_INITDB_ROOT_PASSWORD=
    volumes:
      - discord_db:/data/db
    healthcheck:
      test: mongosh mongo-db:27017/test --tls --tlsCertificateKeyFile /etc/ssl/mongo-db.pem --tlsCAFile /etc/ssl/ca.pem --quiet --eval 'db.runCommand({ping:1})'
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 5s

  # api:
  #   container_name: discord-api
  #   build: ./api
  #   environment:
  #     - API_PORT=8443
  #   ports:
  #     - "8443:8443"
  #   volumes:
  #     - discord_api_ssl_certs:/etc/letsencrypt/live/

  # api:
  #   container_name: discord-web
  #   build: ./web
  #   environment:
  #     - WEB_PORT=8443
  #   ports:
  #     - "8443:8443"
  #   volumes:
  #     - discord_web_ssl_certs:/etc/letsencrypt/live/

volumes:
  discord_cogs:
  discord_git_ssh:
  discord_db:
  #discord_api_ssl_certs:
  #discord_web_ssl_certs:
```

## Required environment variables

- `DISCORD_BOT_DESCRIPTION` - The description of the bot
- `DISCORD_BOT_TOKEN` - Discord Token for your bot from the Discord Developer Portal
- `DISCORD_BOT_OWNER_ID` - The Bot Owner's user id
- `DISCORD_BOT_COMMAND_PREFIX` - Command Prefix Ex. `!`
- `DISCORD_BOT_LOG_LEVEL` - the int log level `(10, 20, 30, 40, 50)`
- `MONGO_INITDB_ROOT_USERNAME` - The root user for MongoDB
- `MONGO_INITDB_ROOT_PASSWORD` - The root password for MongoDB

# Contributing

If you would like to contribute to the project, please read both the [CONTRIBUTING.md](CONTRIBUTING.md) and the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) guidelines.

Features request can be submitted by using [GitHub Issues](https://github.com/xn4p4lm-org/bot-o-cat/issues).

All code, comments, and critiques are greatly appreciated.

# License

Bot-O-Cat and all components are licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
