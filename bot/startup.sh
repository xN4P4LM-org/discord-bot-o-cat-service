#!/bin/bash

# Generate ssh key if it does not exist
if [ ! -f /root/.ssh/id_ed25519 ]; then
  ssh-keygen -t ed25519 -C "Discord Bot" -f /root/.ssh/id_ed25519
fi

# Start the bot
python bot.py