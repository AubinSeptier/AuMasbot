import discord
from discord.ext import commands


class Aide(commands.Cog):
    def __init__(self, client):
        self.client = client

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
        await ctx.message.delete()
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
            value="Faîtes !bonjour et il vous répondra gentilment ",
            inline=True
        )
        e.add_field(
            name="Pour accéder aux infos du serveur",
            value="Faîtes !infoServeur ou !infoserv ou encore !invoServ",
            inline=True
        )
        e.add_field(
            name="Pour créer un sondage",
            value="Faîtes !poll <question> ou !vote <question>",
            inline=True
        )
        await ctx.message.delete()
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
            value="Faîtes !linternet pour une citation aléatoire prise sur internet\n "
                  "!citation <help> pour des citations personnalisées",
            inline=True
        )
        await ctx.message.delete()
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["helpmodo"])
    async def helpmoderate(self, ctx):
        e = discord.Embed(
            title=f"Modération",
            description=f"Vous trouverez ici les commandes de modération",
            color=0x008000
        )
        e.add_field(
            name="Pour effacer un certain nombre de messages",
            value="Faîtes !clear <nombre> ou !delete <nombre>",
            inline=True
        )
        e.add_field(
            name="Pour avertir une personne",
            value="Faîtes !warn <nom> + [raison] ou !attention <nom> + [raison]",
            inline=True
        )
        e.add_field(
            name="Pour kick une personne",
            value="Faîtes !kick <nom> + [raison] ou !kickuser <nom> + [raison]",
            inline=True
        )
        e.add_field(
            name="Pour mute une personne",
            value="Faîtes !mute <nom> + [raison]",
            inline=True
        )
        e.add_field(
            name="Pour unmute une personne",
            value="Faîtes !unmute <nom> + [raison]",
            inline=True
        )
        e.add_field(
            name="Pour bannir une personne",
            value="Faîtes !ban <nom> + |nombre jours| + [raison]",
            inline=True
        )
        e.add_field(
            name="Pour unban une personne",
            value="Faîtes !unban <nom> + [raison]",
            inline=True
        )
        await ctx.message.delete()
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["helpmédia"])
    async def helpmedia(self, ctx):
        e = discord.Embed(
            title=f"Modération",
            description=f"Vous trouverez ici les commandes des différents médias",
            color=0x008000
        )
        await ctx.message.delete()
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Aide(client))
