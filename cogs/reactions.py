
import requests
import discord
from discord.ext import commands


class Reaction(commands.Cog):
    def __init__(self, client):
        """
        La fonction __init__ est appelé à chaque fois qu'un objet est créé à partir d'une classe. La fonction sert à
        initialiser les attributs de l'objet.

        :param self : ce paramètre est utilisé pour représenter l'instance de la classe. On peut donc grâce à lui
        accéder aux attributs et aux méthodes de la classe.
        :param client: il définit notre BOT définit dans la main mais ici on l'initie aussi dans la classe.
        """
        self.client = client

    @commands.command(pass_context=True, aliases=["Salut", "Coucou", "Yo"])
    async def bonjour(self, ctx):
        """
        Fonction qui permet de saluer notre sympathique BOT.

        :param self: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été
        rentrée. Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été
        rentrée. Par exemple le salon Discord, la personne qui a appelée la fonction etc...

        :return: Le bot nous répond aussi en nous saluant.
        """
        await ctx.send('Salut !')

    @commands.command(pass_context=True, aliases=["vote"])
    async def poll(self, ctx, *, message):
        """
        Fonction qui permet de créer un sondage pour n'importe quelle question que l'on veut.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été
        rentrée. Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param message: chaine de caractères correpondant à la question écrite par l'utilisateur de la commande.

        :return: On obtient un sondage avec la question posée avec la possibilité de donner son avis avec des réactions.
        """
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
        """
        Cette fonction tourne en boucle. Elle consiste à regarder tous les messages envoyés, et dès qu'il y a une
        chaine de caractères que le bot reconnaît, il répond avec le mot voulu.

        :param message: chaine de caractères contenant plusieurs mots possibles.

        :return: réponse du bot en fonction du message précédent
        """
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

    @commands.command(aliases=["btc", "$"])
    async def bitcoin(self, ctx):
        """
        Fonction permettant d'obtenir le prix du bitcoin en dollars et en euro à l'instant présent
        @param ctx: nom de la commande à taper

        Récupère dans un fichier .json les informations du lien grâce à la librairie requests
        Puis on récupère les données qui nous intéressent dans des variables en "triant"
        @return: le prix du bitcoin en dollars et euro dans un embed avec images
        """
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        US_price = data["bpi"]["USD"]["rate"]
        EUR_price = data["bpi"]["EUR"]["rate"]
        e = discord.Embed(
            title=f"CryptoMoulaga \U0001F911 \U0001F4B8",
            description=f"\U0001F1FA\U0001F1F8 {US_price}$ \n\U0001F1EA\U0001F1FA {EUR_price}€",
            color=0xF4D03F
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        e.set_image(url="https://c.tenor.com/dWr1cf7RN_gAAAAd/money-wwf.gif")
        e.set_thumbnail(
            url="https://cdn.futura-sciences.com/buildsv6/images/wide1920/b/8/9/b894848516_50174405_bourse-chute.jpg")
        await ctx.message.delete()
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Reaction(client))
