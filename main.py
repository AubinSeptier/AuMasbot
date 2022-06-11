import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True
load_dotenv('.env')

desc = "Bot créé par **Aubin** et **Thomas**\n " \
        "Je suis ici pour faire de la modération mais aussi pour vous divertir !\n" \
        "Tapez **!help** pour avoir plus d'informations sur mes fonctionnalités ! \U0001F604\n\n " \
       "Pour suivre l'actualité de notre école :\n " \
       "-https://www.instagram.com/bde_mega/\n -https://www.instagram.com/esiremdijon/ " \


client = commands.Bot(command_prefix='!', description=desc, intents=intents, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='ESIREM'))
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
