import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
load_dotenv('.env')
client = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@client.event
async def on_ready():
    print("Je suis prêt")


# Recherche des fichiers python avec les cogs
for fn in os.listdir("cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")


# Chargement des cogs
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Cog chargée")


# Déchargement des cogs
@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("Cog déchargée")


# Rechargement des cogs
@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send("Cog rechargée")


####


######
# Démarre le bot
client.run(os.getenv('DISCORD_TOKEN'))
