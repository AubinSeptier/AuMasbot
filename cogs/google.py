import random

import discord
from discord.ext import commands
from googleapiclient.discovery import build

intents = discord.Intents.default()
intents.members = True
API_KEY = "AIzaSyCG7yr5OD4FgAm6tSSw27gm0F-UAbVT_A4"


class Google(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["goog", "search"])
    async def google(self, ctx, *, search):
        key = API_KEY
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=key).cse
        image = resource.list(
            q=f"{search}", cx="fbd05fa2f88bc290c", searchType="image"
        ).execute()
        url = image["items"][ran]["link"]
        embed1 = discord.Embed(title=f"AuMasBot Image: ({search.title()})")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)

    @commands.command(aliases=["show"])
    async def showpic(self, ctx, *, search):
        key = API_KEY
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=key).cse()
        result = resource.list(
            q=f"{search}", cx="fbd05fa2f88bc290c", searchType="image"
        ).execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"Here Your Image ({search}) Feature made by BOR NATION on YT")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)


# Initialise le cog
def setup(client):
    client.add_cog(Google(client))
