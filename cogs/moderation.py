import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(pass_context = True, name = "ban", aliases = ["bannir"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, jours: int, *, raison=""):
        await member.ban(reason=raison, delete_message_days = jours)
        e = discord.Embed(
            title=f"{member} a été banni du serveur.",
            description=f"Raison du bannissement : {raison}",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(pass_context = True, name = "kick", aliases = ["kickuser"])
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

    @commands.command()
    async def clear(self, ctx, nombre: int):
        messages = await ctx.channel.history(total=nombre + 1).flatten()
        for message in messages:
            await message.delete()


    @commands.command()
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


