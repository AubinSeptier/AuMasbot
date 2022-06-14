import json
import random

import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


# Classe avec les events citations
class Citation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Fonction permettant de générer des citations personnalisées avec une commande
    @commands.command(aliases=["quote", "cita"])
    async def citation(self, ctx, quote):
        """

        @param ctx: nom de la commande à taper
        @param quote: argumant choisissant la citation selon le mot-clé attribué

        quote_list: liste des citations disponibles
        quote_list_name: liste des noms des citations disponibles
        Utilisation de if pour sélectionner la citation demander selon le mot-clé
        @return: retourne la citation dans un embed
        """
        quote_list = ["Oui c'est ça", "Très réel ça", "Ah ouais", "Ratio", "ff", "Je code un bot python",
                      "Je suis Aumasbot!"]
        quote_list_name = "random / wormix / tomichou / adilou / ratio / ff / python / ..."
        if quote == "help":
            send_quote = (f"Citations disponibles: {quote_list_name}")
        if quote == "random":
            send_quote = random.choice(quote_list)
        if quote == "thomi":
            send_quote = quote_list[0]
        if quote == "thomichou":
            send_quote = quote_list[1]
        if quote == "adilou":
            send_quote = quote_list[2]
        if quote == "ratio":
            send_quote = quote_list[3]
        if quote == "ff":
            send_quote = quote_list[4]
        if quote == "python":
            send_quote = quote_list[5]
        if quote == "aumasbot":
            send_quote = quote_list[6]
        e = discord.Embed(
            title=f"{send_quote}",
            color=0x6F0098
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=e)

    @commands.command(name="famous", aliases=["inspiration", "people"])
    async def internet_citation(self, ctx):
        """
        Fonction permettant de générer aléatoirement une citation célèbre en anglais
        @param ctx: nom de la commande à taper

        Récupère les données du lien dans un fichier text en javascript grâce à la librairie requests
        Charge le fichier et stocke la citation et l'auteur associé dans une variable
        @return: la citation dans un embed
        """
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        internet_quote = json_data[0]['q'] + "\n                                                    " \
                                             "             " + json_data[0]['a']
        e = discord.Embed(
            title=f"{internet_quote}",
            color=0x6F0098
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=e)

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


# Initialise le cog
def setup(client):
    client.add_cog(Citation(client))
