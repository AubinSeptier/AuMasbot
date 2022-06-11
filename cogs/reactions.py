from random import randint
import discord
from discord.ext import commands


class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=["Salut", "Coucou", "Yo"])
    async def bonjour(self, ctx):
        await ctx.send('Salut !')

    @commands.command(pass_context=True, aliases=["dices", "dés", "dé"])
    async def dice(self, ctx, nombre: int):
        result = randint(1, nombre)  # Prend un nombre aléatoire entre 1 et nombre
        diceEmbed = discord.Embed(title=f"Tirage d'un dé de {nombre} !", description=f"Le dé est tombé sur {result} !",
                                  color=0x0080ff)
        diceEmbed.set_footer(text=f"Tirage effectué par {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=diceEmbed)

    @commands.command(pass_context=True, aliases=["vote"])
    async def poll(self, ctx, *, message):
        pollEmbed = discord.Embed(title="Nouveau Sondage!", description=f"{message}", color=0x0080ff)
        pollEmbed.set_footer(text=f"Sondage émis par {ctx.author}", icon_url=ctx.author.avatar_url)
        pollEmbed.timestamp = ctx.message.created_at
        await ctx.message.delete()
        poll_msg = await ctx.send(embed=pollEmbed)

        await poll_msg.add_reaction("✅")
        await poll_msg.add_reaction("⭕")
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, message):

        if 'quoi' in message.content.lower():
            await message.channel.send("feur")

        if message.content.lower() == "oui":
            await message.channel.send("stiti")

        if message.content.lower() == "wesh":
            await message.channel.send("dene")

        if 'ouai' in message.content.lower():
            await message.channel.send("stern")
        elif 'ouais' in message.content.lower():
            await message.channel.send("tern")

        if message.content.lower() == "comment":
            await message.channel.send("aire")

        if message.content.lower() == "non":
            await message.channel.send("bril")

        if message.content.lower() == "ping":
            await message.channel.send("pong")


def setup(client):
    client.add_cog(Reaction(client))
