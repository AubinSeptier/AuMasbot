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

    # Fonction permettant de générer aléatoirement une citation célèbre en anglais
    @commands.command(name="famous", aliases=["inspiration", "people"])
    async def internet_citation(self, ctx):
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


# Initialise le cog
def setup(client):
    client.add_cog(Citation(client))
