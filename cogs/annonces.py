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
        e=discord.Embed(
            title=f"{member.name} a rejoint le serveur",
            color=0x008000
        )
        await channel.send(embed=e)

    # Event pour départ d'un membre du serveur
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(970243343441362946)
        e=discord.Embed(
            title=f"{member.name} a quitté le serveur",
            color=0x008000
        )
        await channel.send(embed=e)

    ## Annonce les suppressions de messages
    #@commands.Cog.listener()
    #async def on_message_delete(self, message):
    #    await message.channel.send(f'{message.author} a supprimé un message')  # delete_after=5


# Initialise le cog
def setup(client):
    client.add_cog(Annonce(client))
