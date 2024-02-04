#!/bin/bash

# upgrade pip
pip install --upgrade pip

# install pip dev dependencies
pip install -r requirements-dev.txt

# welcome message
echo "Welcome to the bot-o-cat development environment!"