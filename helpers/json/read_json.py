"""
This module contains functions to read json files.
"""
import json
import os


def readJson(path) -> dict | list:
    """Reads the json file(s) and returns the data as a dictionary."""

    read_json = {}

    if os.path.isdir(path):
        # load all json files from the given directory and return them in a dictionary
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(f"{path}/{filename}", encoding="utf-8") as json_file:
                    read_json[filename[:-5]] = json.load(json_file)
    elif os.path.isfile(path) and path.endswith(".json"):
        # load a single json file and return it as a dictionary
        with open(path, encoding="utf-8") as json_file:
            return json.load(json_file)

    return read_json
