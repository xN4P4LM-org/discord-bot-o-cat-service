# Use the official Python base image
FROM python:latest

# Set the working directory inside the container
WORKDIR /bot

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-setuptools \
    python3-venv \
    python3-pip \
    gcc

COPY requirements.txt requirements.txt

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the bot code to the container
COPY . .

# Run the bot
ENTRYPOINT "/bot/startup.sh"
