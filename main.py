import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
load_dotenv('.env')
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    """
    Indique dans la console quand le bot est prêt
    """
    print("Je suis prêt")


# Recherche des fichiers python avec les cogs
for fn in os.listdir("cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")


# Chargement des cogs
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    """
    Fonction permettant de charger les cogs contenus dans le fichier cogs afin de les activer sur le serveur
    @param ctx: nom de la commande à taper
    @param extension: extension du fichiers à charger
    """
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Cog chargée")


# Déchargement des cogs
@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    """
    Fonction permettant de décharger les cogs contenus dans le fichier cogs afin de les désactiver sur le serveur
    @param ctx: nom de la commande à taper
    @param extension: extension du fichiers à décharger
    """
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("Cog déchargée")


# Rechargement des cogs
@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    """
    Fonction permettant de recharger les cogs contenus dans le fichier cogs
    @param ctx: nom de la commande à taper
    @param extension: extension du fichiers à décharger
    """
    client.reload_extension(f"cogs.{extension}")
    await ctx.send("Cog rechargée")


####


######
# Démarre le bot
client.run(os.getenv('DISCORD_TOKEN'))
