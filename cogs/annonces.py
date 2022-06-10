import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


# Classe avec les events annonces
class Annonce(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Event pour arrivée d'un membre sur le serveur
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("Bienvenue sur le serveur")
        channel = member.guild.get_channel(970243343441362946)
        await channel.send(f"{member.mention} a rejoint le serveur")

    # Event pour départ d'un membre du serveur
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(970243343441362946)
        await channel.send(f"{member.mention} a quitté le serveur")


# Initialise le cog
def setup(client):
    client.add_cog(Annonce(client))
