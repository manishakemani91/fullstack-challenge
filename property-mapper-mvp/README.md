# Property Mapper Application

This project is a full-stack application designed to help users track property data on a map, allowing them to easily locate specific properties. The application consists of a backend and frontend component, managed using Docker and Docker Compose.

## Table of Contents

- [Application Overview](#application-overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running Locally](#running-locally)
- [Directory Structure](#directory-structure)
- [Troubleshooting](#troubleshooting)

## Application Overview

The Property Mapper Application allows users to track and visualize property data on a map, providing an intuitive interface for locating specific properties.

## Prerequisites

Ensure that you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/manishakemani91/fullstack-challenge.git
   cd property-mapper-mvp

2. **Run the start.sh Script**

    The start.sh script will build and start the Docker containers for the entire application. Make the script executable and run it:
    ```bash
    chmod +x start.sh
    ./start.sh

    This script will:

    Build Docker images for the backend and frontend.
    Start the Docker containers for both services.

3. **Access the Application**

    Frontend: Open your web browser and navigate to http://localhost:8080.
    Backend: The backend service will be accessible at http://localhost:8000.

## Running Locally

    For development purposes, you can run the backend and frontend services separately. Follow the instructions in their respective README.md files for local setup.

Backend

    Navigate to the backend directory.
    Refer to the [README.md](https://github.com/manishakemani91/fullstack-challenge/blob/master/property-mapper-mvp/backend/README.md) file in the backend directory for setup and running instructions.

Frontend

    Navigate to the frontend directory.
    Refer to the [README.md](https://github.com/manishakemani91/fullstack-challenge/blob/master/property-mapper-mvp/frontend/README.md) file in the frontend directory for setup and running instructions.

## Directory Structure

    property-mapper-app/
    ├── backend/
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── app/
    │   └── ...
    ├── frontend/
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── src/
    │   └── ...
    ├── start.sh
    ├── docker-compose.yml
    └── README.md

    backend/: Contains the backend code and Dockerfile.
    frontend/: Contains the frontend code and Dockerfile.
    start.sh: A script to bring up the Docker containers for the application.
    docker-compose.yml: Docker Compose configuration file for defining and running the multi-container Docker applications.

## Troubleshooting

    Containers Not Starting: Ensure Docker and Docker Compose are properly installed and running on your system. Check for any errors in the start.sh script or Docker logs.

    Configuration Issues: Verify that your .env files or environment variables are correctly set up. Refer to the individual README.md files for configuration details.


