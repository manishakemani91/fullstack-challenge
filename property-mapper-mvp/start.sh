#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Docker is installed
if ! command_exists docker; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Check if Docker Compose is installed
if ! command_exists docker-compose; then
    echo "Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

cd "$(dirname "$0")"

# Start Docker Compose
echo "Starting Docker Compose..."
docker-compose up -d

if [ $? -eq 0 ]; then
    echo "Docker containers are up and running."
else
    echo "Failed to start Docker containers."
    exit 1
fi
