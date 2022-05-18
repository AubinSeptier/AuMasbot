import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, name="infoServeur", aliases=["infoServ", "infoserv"])
    async def infoServeur(self, ctx):
        server = ctx.guild
        numberOfTextChannels = len(server.text_channels)
        numberOfVoiceChannels = len(server.voice_channels)
        serverDescription = server.description
        numberOfPerson = server.member_count
        serverName = server.name
        e = discord.Embed(
            title=f"Infos serveur",
            description=f"Bonjour ! \U0001F603\nLe serveur **{serverName}** contient {numberOfPerson} personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux. \n\nOn voit souhaite un très bon amusement sur **{serverName}** ! \U0001F609",
            color=0x008000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)


    @commands.command(pass_context = True, name = "ban", aliases = ["bannir"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, jours: int, *, raison=""):
        await member.ban(reason=raison, delete_message_days=jours)
        e = discord.Embed(
            title=f"{member} a été banni du serveur.",
            description=f"Raison du bannissement : {raison}",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(pass_context = True, name="kick", aliases = ["kickuser"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, raison=""):
        await member.kick(reason=raison)
        e = discord.Embed(
            title=f"{member} a été kick.",
            description=f"Raison : `{raison}`",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(pass_context=True, name="clear", aliases=["delete", "del", "suppr"])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)
        e = discord.Embed(
            title=f"{limit} messages ont été supprimé.",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(pass_context=True, name="warn", aliases=["attention", "achtung"])
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, raison=""):
        e = discord.Embed(
            title=f"{member} vous avez un avertissement, attention à vous !",
            description=f"Raison : `{raison}`",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user, *reason):
        reason = " ".join(reason)
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user, reason=reason)
                await ctx.send(f"{user} à été unban.")
                return

        await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")  # Si l'utilisateur n'a pas été trouvé


def setup(client):
    client.add_cog(Moderation(client))


