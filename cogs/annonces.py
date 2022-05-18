import discord
from discord.ext import commands


# Classe avec les events annonces
class Annonce(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Salut les nouveaux arrivants
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Bienvenue {member.name} sur le serveur!'
        )
        await member.channel.send(f'{member.name} est arrivé sur le serveur')

    # Annonce les suppressions de messages
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await message.channel.send(f'{message.author} a supprimé un message')

    @commands.command()
    async def blc(self, ctx):
        await ctx.send('Nique sa race!')


# Initialise le cog
def setup(client):
    client.add_cog(Annonce(client))
