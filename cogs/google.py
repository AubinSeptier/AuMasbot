import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv('.env')

intents = discord.Intents.default()
intents.members = True


class Google(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["goog", "search"])
    async def google(self, ctx, *, search):
        key = os.getenv('API_KEY')
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=os.getenv('API_KEY')).cse()
        result = resource.list(
            q=f"{search}", cx="fbd05fa2f88bc290c", searchType="image"
        ).execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"AuMasBot Image: {search}")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)


# Initialise le cog
def setup(client):
    client.add_cog(Google(client))
