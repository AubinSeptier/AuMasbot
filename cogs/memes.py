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
        e = discord.Embed(title="Meme de Reddit", color=0x0080ff)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                e.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                e.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.message.delete()
                await ctx.send(embed=e)

    #Fonction permettant de générer des memes personnalisées
    @commands.command()
    async def meme(self, ctx, image):
        memes_list = ["https://imgur.com/gallery/lN0O6Zf.gif", "https://imgur.com/gallery/cuq7xl7.gif",
                    "https://i.imgur.com/xX04UWu.jpg", "https://i.imgflip.com/6hza7t.jpg",
                      "https://i.imgflip.com/6h8gjb.jpg", "https://i.imgflip.com/6iuzcj.jpg",
                      "https://i.imgflip.com/6iv0g7.jpg", "https://i.imgflip.com/6iv4cv.jpg",
                      "https://i.imgflip.com/6iv5b3.jpg", "https://i.imgflip.com/6iv6b4.jpg",
                      "https://i.imgflip.com/6iv6yu.jpg"]
        await ctx.message.delete()
        if image == "random":
            await ctx.send(random.choice(memes_list))
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
        if image == "wormix":
            await ctx.send(memes_list[5])
        if image == "maths":
            await ctx.send(memes_list[6])
        if image == "wormax":
            await ctx.send(memes_list[7])
        if image == "top":
            await ctx.send(memes_list[8])
        if image == "ego":
            await ctx.send(memes_list[9])
        if image == "carry":
            await ctx.send(memes_list[10])

# Initialise le cog
def setup(client):
    client.add_cog(MemeGenerator(client))
