import random

import aiohttp
import discord
from discord.ext import commands


class MemeGenerator(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Fonction permettant de générer des memes venant du fil Reddit "r/memes"
    @commands.command(aliases=["reddit", "lol"])
    async def rmeme(self, ctx):
        embed = discord.Embed(title="Meme", description="Petit Meme Sympathique (PMS)")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    #Fonction permettant de générer des memes personnalisées
    @commands.command()
    async def meme(self, ctx, image):
        memes_list = ["https://imgur.com/gallery/lN0O6Zf.gif", "https://imgur.com/gallery/cuq7xl7.gif",
                    "https://i.imgur.com/xX04UWu.jpg", "https://i.imgflip.com/6hza7t.jpg",
                      "https://i.imgflip.com/6h8gjb.jpg"]
        if image == "guys":
            await ctx.send(memes_list[0])
        if image == "pikachu":
            await ctx.send(memes_list[1])
        if image == "gaming1":
            await ctx.send(memes_list[2])
        if image == "china":
            await ctx.send(memes_list[3])
        if image == "sleep":
            await ctx.send(memes_list[4])
        if image == "":
            await ctx.send(memes_list[5])

# Initialise le cog
def setup(client):
    client.add_cog(MemeGenerator(client))
