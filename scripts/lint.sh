#!/bin/bash

# Run pylint on all python files in the project
find bot/ ! -path "./.venv/*" -type f -name "*.py"  | xargs pylint --rcfile pylintrc