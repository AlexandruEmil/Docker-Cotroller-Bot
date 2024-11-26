import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from DockerManager import DockerManager

# Încarcă variabilele din .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DOCKER_HOST = os.getenv("DOCKER_HOST")

# Instanță pentru DockerManager
docker_manager = DockerManager(DOCKER_HOST)

# Configurare bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Botul este online ca {bot.user}")

@bot.command()
async def list(ctx):
    containers = docker_manager.list_containers()
    await ctx.send("\n".join(containers) if containers else "Nu există containere.")

@bot.command()
async def start(ctx, name: str):
    response = docker_manager.start_container(name)
    await ctx.send(response)

@bot.command()
async def stop(ctx, name: str):
    response = docker_manager.stop_container(name)
    await ctx.send(response)

@bot.command()
async def restart(ctx, name: str):
    response = docker_manager.restart_container(name)
    await ctx.send(response)

bot.run(TOKEN)
