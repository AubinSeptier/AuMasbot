import discord
import os
import annonces
from dotenv import load_dotenv

load_dotenv('.env')
client = discord.Client()


@client.event
async def on_ready():
    print("Je suis prêt")


client.run(os.getenv('DISCORD_TOKEN'))