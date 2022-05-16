import discord
from discord.ext import commands
client = commands.Bot(command_prefix="!", help_command=None)

client = discord.Client()

@client.command(pass_context = True, name = "ban", aliases = ["bannir"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, jours: int, *, raison=""):
    await member.ban(reason=raison, delete_message_days=jours)
    e = discord.Embed(
        title=f"{ctx.message.author.name} a été banni du serveur.",
        description=f"Raison du bannissement : {raison}",
        color=0xff0000
    )
    e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=e)


@client.command(pass_context = True, name = "kick", aliases = ["kickuser"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, raison=""):
    await member.kick(reason=raison)
    e = discord.Embed(
        title=f"{ctx.message.author.name} a été kick.",
        description=f"Raison du kick : `{raison}`",
        color=0xff0000
    )
    e.set_author(name = ctx.message.author.name,icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed=e)


@client.command()
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(total=nombre + 1).flatten()
    for message in messages:
        await message.delete()


@client.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return

    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")  # Si l'utilisateur n'a pas été trouvé




