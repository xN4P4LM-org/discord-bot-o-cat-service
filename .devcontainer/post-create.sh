#!/bin/bash

# upgrade pip
pip install --upgrade pip

# install pip dev dependencies
pip install -r bot/requirements-dev.txt

# pull most recent submodules
git submodule update --init --recursive

# welcome message
echo "Welcome to the bot-o-cat development environment!"