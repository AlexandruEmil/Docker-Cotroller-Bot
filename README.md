# Docker-Cotroller-Bot

A Discord bot that allows you to manage Docker containers directly from your Discord server. This project provides an interactive and user-friendly way to control Docker containers using Discord text commands.
# Key Features

   List Containers: Displays all Docker containers, including their status (running/stopped). \
   Start Containers: Allows starting a specific container. \
   Stop Containers: Allows stopping a specific container. \
   Restart Containers: Restarts a specific container. 

# How It Works

The bot uses the ```discord.py``` library to interact with Discord and the docker library to communicate with the Docker daemon. On Windows, it connects to Docker via Named Pipes, while on Linux, it uses the UNIX socket.
# Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/AlexandruEmil/docker-controller-bot.git
```
```
cd docker-controller-bot
```
### 2. Create and configure a .env file
```
DISCORD_TOKEN=your_bot_token
```
```
DOCKER_HOST=npipe:////./pipe/docker_engine # for Windows
```
### 3. Build the Docker image
```
docker build -t docker-controller-bot .
```
### 4. Run the container
```
docker run -d --name docker-bot \
    --env-file .env \
    -v //./pipe/docker_engine://./pipe/docker_engine \
    docker-controller-bot
```

# Available Commands

  ```!list: Lists all Docker containers and their current status.``` \
  ```!start <name>: Starts a specific container.``` \
  ```!stop <name>: Stops a specific container.``` \
  ```!restart <name>: Restarts a specific container.```

# Technologies Used
```
  Python 3.10+
    Libraries:
        discord.py: For Discord interactions
        docker: To manage Docker containers
        python-dotenv: To handle environment variables
    Docker: Containerization platform
```
# System Requirements
  Python 3.10+
  Docker Desktop (for Windows) or Docker Engine (for Linux)
  A Discord bot set up via the ```Discord Developer Portal```

# Contributing

If you have suggestions, feature requests, or bug reports, feel free to open an issue or submit a pull request.
