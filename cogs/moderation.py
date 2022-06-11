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
            description=f"Bonjour ! \U0001F603\nLe serveur **{serverName}** contient {numberOfPerson} personnes ! \n"
                        f"La description du serveur est {serverDescription}. \n"
                        f"Ce serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon "
                        f"vocaux, de quoi s'exprimer et donc de s'amuser ! \n\n"
                        f"On voit souhaite un très bon amusement sur **{serverName}** ! \U0001F609",
            color=0x008000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
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
        await ctx.message.delete()
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
        await ctx.message.delete()
        await ctx.send(embed=e)

    @commands.command(pass_context=True, name="clear", aliases=["delete", "del", "suppr"])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        e = discord.Embed(
            title=f"{limit} messages ont été supprimé.",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
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
        await ctx.message.delete()
        await ctx.send(embed=e)

    async def createMutedRole(self, ctx):
        mutedRole = await ctx.guild.create_role(name="Muted",
                                                permissions=discord.Permissions(send_messages=False, speak=False),
                                                read_message_history=True, read_messages=True,
                                                reason="Creation du role Muted pour mute des gens.")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, send_messages=False, speak=False, read_message_history=True,
                                          read_messages=True)
        return mutedRole

    async def getMutedRole(self, ctx):
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Muted":
                return role
        return await self.createMutedRole(ctx)

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
        mutedRole = await self.getMutedRole(ctx)
        await member.add_roles(mutedRole, reason=reason)
        e = discord.Embed(
            title=f"{member} a été mute !",
            description=f"Raison : `{reason}`",
            color=0xff7f00
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=e)

    @commands.command()
    async def unmute(self, ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
        mutedRole = await self.getMutedRole(ctx)
        await member.remove_roles(mutedRole, reason=reason)
        e = discord.Embed(
            title=f"{member} a été unmute, bon retour parmi nous !",
            description=f"Raison : `{reason}`",
            color=0xff7f00
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Moderation(client))
