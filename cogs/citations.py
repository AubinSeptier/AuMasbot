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

    @commands.command(aliases=["quote", "cita"])
    async def citation(self, ctx, quote):
        quote_list = ["Oui c'est ça", "Très réel ça", "Ah ouais", "Ratio", "ff", "Je code un bot python",
                      "Je suis Aumasbot!"]
        quote_list_name = "random / wormix / tomichou / adilou / ratio / ff / python / ..."
        send_quote = str("None")
        if quote == "help":
            await ctx.send(f"Citations disponibles: {quote_list_name}")
        if quote == "random":
            await ctx.send(random.choice(quote_list))
        if quote == "wormix":
            send_quote = quote_list[0]
        if quote == "tomichou":
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
        await ctx.send(send_quote)

    @commands.command(aliases=["linternet"])
    async def internet_citation(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)


# Initialise le cog
def setup(client):
    client.add_cog(Citation(client))
