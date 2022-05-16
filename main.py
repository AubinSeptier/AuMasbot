import discord
import os
import annonces
from dotenv import load_dotenv
from discord.ext import commands
client = commands.Bot(command_prefix="!", help_command=None)

load_dotenv('.env')

client = discord.Client()


@client.event
async def on_ready():
    print("Je suis prêt")


client.run(os.getenv('DISCORD_TOKEN'))