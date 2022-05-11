import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

client = discord.Client()


@client.event
async def on_ready():
    print("Je suis prêt")


client.run(os.getenv("TOKEN"))
