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
        e = discord.Embed(
            title=f"Tirage du dé !",
            description=f"Le dé est tombé sur {result} !",
            color=0x0080ff
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

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
