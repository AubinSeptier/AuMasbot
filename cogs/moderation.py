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
            description=f"Bonjour ! \U0001F603\nLe serveur **{serverName}** contient {numberOfPerson} personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux, de quoi s'exprimer et donc de s'amuser ! \n\nOn voit souhaite un très bon amusement sur **{serverName}** ! \U0001F609",
            color=0x008000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(pass_context=True, name="ban", aliases=["bannir"])
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

    @commands.command(pass_context=True, name="kick", aliases=["kickuser"])
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
        await ctx.channel.purge(limit=limit + 1)
        e = discord.Embed(
            title=f"{limit} messages ont été supprimés.",
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
    async def unban(self, ctx, member: discord.Member):  # on travaille dessus mais pas fonctionnel encore
        memberName, memberId = member.split("#")
        bannedMembers = await ctx.guild.bans()
        for i in bannedMembers:
            if i.member.name == memberName and i.member.discriminator == memberId:
                await ctx.guild.unban(i.member)
                await ctx.send(f"{member} à été unban.")
                return

        await ctx.send(
            f"L'utilisateur {member} n'est pas dans la liste des bans")  ##  # Si l'utilisateur n'a pas été trouvé

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def massunban(self, ctx):
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await ctx.guild.unban(user=users.user)
            except:
                pass
        e = discord.Embed(
            title="La prison des bannis est ouverte !",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

def setup(client):
    client.add_cog(Moderation(client))
