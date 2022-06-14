import random

import aiohttp  # Framework permettant une connection client/serveur avec un protocole HTTP
import discord
from discord.ext import commands


class MemeGenerator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["reddit", "lol"])
    async def rmeme(self, ctx):
        """
        Fonction permettant de générer des memes venant du fil Reddit "r/memes"
        @param ctx: nom de la commande à taper

        Récupère les inforomations du fil reddit et dans un fichier .json à l'aide de la librairie aiohttp
        Sélectionne de façon random le meme à partir du fichier .json
        Retourne le meme dans un embed
        """
        e = discord.Embed(title="Meme de Reddit", color=0x0080ff)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                e.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                e.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.message.delete()
                await ctx.send(embed=e)

    @commands.command()
    async def meme(self, ctx, image):
        """
        Fonction permettant de générer des memes personnalisés/customisés/spécifiques
        @param ctx: nom de la commande à taper
        @param image: argumant choisissant l'image selon le mot-clé attribué

        memes_list: liste contenant les différents liens des memes
        Utilise des if afin de choisir la bonne image en utilisant une variable "meme_choice"
        Retourne le meme choisi dans le channel où a été fait la demande
        """
        memes_list = ["https://imgur.com/gallery/lN0O6Zf.gif", "https://imgur.com/gallery/cuq7xl7.gif",
                      "https://i.imgur.com/xX04UWu.jpg", "https://i.imgflip.com/6hza7t.jpg",
                      "https://i.imgflip.com/6h8gjb.jpg", "https://i.imgflip.com/6iuzcj.jpg",
                      "https://i.imgflip.com/6iv0g7.jpg", "https://i.imgflip.com/6iv4cv.jpg",
                      "https://i.imgflip.com/6iv5b3.jpg", "https://i.imgflip.com/6iv6b4.jpg",
                      "https://i.imgflip.com/6iv6yu.jpg"]
        await ctx.message.delete()
        if image == "random":
            meme_choice = (random.choice(memes_list))
        if image == "guys":
            meme_choice = (memes_list[0])
        if image == "pikachu":
            meme_choice = (memes_list[1])
        if image == "gaming1":
            meme_choice = (memes_list[2])
        if image == "china":
            meme_choice = (memes_list[3])
        if image == "sleep":
            meme_choice = (memes_list[4])
        if image == "wormix":
            meme_choice = (memes_list[5])
        if image == "maths":
            meme_choice = (memes_list[6])
        if image == "wormax":
            meme_choice = (memes_list[7])
        if image == "top":
            meme_choice = (memes_list[8])
        if image == "ego":
            meme_choice = (memes_list[9])
        if image == "carry":
            meme_choice = (memes_list[10])
        await ctx.send(meme_choice)

    @commands.command()
    async def goat(self, ctx):
        """
        Donne le lien du Youtube du meilleur influenceur de France
        @param ctx: nom de la commande à taper

        Récupération du lien dans "link", suppression de la commande dans le channel et ajout d'un embed
        Retourne un embed avec le lien de la chaine et une image
        """
        link = "https://www.youtube.com/c/MattPna"
        await ctx.message.delete()
        e = discord.Embed(title="The GOAT Maatiou", description=f"Toutube: {link}")
        e.set_image(url="https://i.ytimg.com/vi/49UXUbORp0A/maxresdefault.jpg")
        await ctx.send(embed=e)


# Initialise le cog
def setup(client):
    client.add_cog(MemeGenerator(client))
