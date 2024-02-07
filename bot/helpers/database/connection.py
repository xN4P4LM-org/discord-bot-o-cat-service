"""
Class for the database configuration for the bot and all cogs.
"""

import os
import sys
import logging
from pymongo import MongoClient

def getDbConnection() -> MongoClient:
    """
    Connects and returns a mongoDB Client.

    Using either the following environment variables or default values:
        - DISCORD_MONGO_DB_HOST_NAME
        - DISCORD_MONGO_DB_PORT
        - DISCORD_MONGO_DB_DATABASE_NAME
    """

    # The certificate file for the database are located:
    # - /etc/ssl/bot.pem
    # - /etc/ssl/ca.pem

    # get the host name
    host = os.getenv("DISCORD_MONGO_DB_HOST_NAME",None)

    # get the port
    port = os.getenv("DISCORD_MONGO_DB_PORT",None)

    if host and port is not None:
        # connect to the database
        db_conn = MongoClient(
            host,
            int(port),
            tls=True,
            tlsCRLFile="/etc/ssl/ca.pem",
            tlsCertificateKeyFile="/etc/ssl/bot.pem"
        )

        return db_conn

    logging.error("Missing environment variables for the database connection.")
    sys.exit(1)