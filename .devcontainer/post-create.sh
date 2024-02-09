#!/bin/bash

# upgrade pip
pip install --upgrade pip

# pull most recent submodules
GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git submodule update --init --recursive

# install pip dev dependencies
pip install -r bot/requirements-dev.txt

# welcome message
echo "Welcome to the bot-o-cat development environment!"