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
        diceEmbed = discord.Embed(title=f"Tirage d'un dé de {nombre} !", description=f"Le dé est tombé sur {result} !", color=0x0080ff)
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

    @commands.command(pass_context=True, aliases=["aide", "ALED"])
    async def help(self, ctx):
        e = discord.Embed(
            title=f"Page d'aide",
            description=f"Vous trouverez ici les commandes selon les fonctionnalités recherchées",
            color=0x008000
        )
        e.add_field(
            name="Pour accéder aux commandes de bases",
            value="Faîtes !helpbase ou !helpdebut ou encore !helpracine",
            inline=True
        )
        e.add_field(
            name="Pour accéder aux commandes de modération",
            value="Faîtes !helpmodo ou !helpmoderate",
            inline=True
        )
        e.add_field(
            name="Pour accéder aux commandes de divertissement",
            value="Faîtes !helpdiv ou !helpdivert ou encore !helpentertainment",
            inline=True
        )
        e.add_field(
            name="Pour accéder aux commandes des différents médias",
            value="Faîtes !helpmedia ou !helpmédia",
            inline=True
        )
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["helpracine", "helpdebut"])
    async def helpbase(self, ctx):
        e = discord.Embed(
            title=f"Commandes de base",
            description=f"Vous trouverez ici les commandes de base",
            color=0x008000
        )
        e.add_field(
            name="Pour saluer notre super bot",
            value="Faîtes !bonjour",
            inline=True
        )
        e.add_field(
            name="Pour accéder aux infos du serveur",
            value="Faîtes !infoServeur ou !infoserv ou encore !invoServ",
            inline=True
        )
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["helpdivert", "helpentertainment"])
    async def helpdiv(self, ctx):
        e = discord.Embed(
            title=f"Commandes de divertissement",
            description=f"Vous trouverez ici les commandes de divertissement",
            color=0x008000
        )
        e.add_field(
            name="Pour lancer un dé",
            value="Faîtes !dice <nombre> ou !dés <nombre> ou encore !dé <nombre>",
            inline=True
        )
        e.add_field(
            name="Pour avoir un meme aléatoire",
            value="Faîtes !rmeme (il vient tout droit de reddit !) ou !meme",
            inline=True
        )
        e.add_field(
            name="Pour avoir une citation",
            value="Faîtes !linternet pour une citation aléatoire prise sur internet\n !citation <help> pour des citations personnalisées",
            inline=True
        )
        e.add_field(
            name="Pour créer un sondage",
            value="Faîtes !poll <question> ou !vote <question>",
            inline=True
        )
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["helpmodo"])
    async def helpmoderate(self, ctx):
        e = discord.Embed(
            title=f"Modération",
            description=f"Vous trouverez ici les commandes de modération",
            color=0x008000
        )
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["helpmédia"])
    async def helpmedia(self, ctx):
        e = discord.Embed(
            title=f"Modération",
            description=f"Vous trouverez ici les commandes des différents médias",
            color=0x008000
        )
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
