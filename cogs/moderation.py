import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        """
        La fonction __init__ est appelé à chaque fois qu'un objet est créé à partir d'une classe. La fonction sert à
        initialiser les attributs de l'objet.

        :param self : ce paramètre est utilisé pour représenter l'instance de la classe. On peut donc grâce à lui
        accéder aux attributs et aux méthodes de la classe.
        :param client: il définit notre BOT définit dans la main mais ici on l'initie aussi dans la classe.
        """
        self.client = client

    @commands.command(pass_context=True, name="infoServeur", aliases=["infoServ", "infoserv"])
    async def infoServeur(self, ctx):
        """
        Cette fonction permet d'obtenir les informations à propos du serveur.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...

        :return: en retour on a un message du bot avec toutes les informations importantes à propos du serveur.
        """
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
        """
        Fonction qui permet de bannir une personne du serveur. C'est-à-dire que la personne est forcée de quitter le
        serveur et qu'elle ne pourra plus le rejoindre.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param member: chaine de caractères correspondant au nom du membre.
        :param jours: integer du nombre de jours pendant lesquels les messages de la personnes sont supprimés.
        :param raison: chaine de caractères correspondant à la raison.

        :return: On a un message du bot attestant du banissement de la personne.
        """
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
        """
        Fonction qui permet d'exclure une personne du serveur. Contrairement au ban, la personne pourra rejoindre le serveur avec une invitation.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param member: chaine de caractères correspondant au nom du membre.
        :param raison: chaine de caractères correspondant à la raison.

        :return: On a un message du bot attestant de l'exclusion de la personne.
        """
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
        """
        Fonction qui permet de supprimer le nombre de messages que l'on veut.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param limit: integer qui représente le nombre de message que l'on souhaite supprimer dans le channel.

        :return: On a un message du bot attestant de la suppression des messages.
        """
        await ctx.channel.purge(limit=limit + 1)
        e = discord.Embed(
            title=f"{limit} messages ont été supprimé.",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)
        await ctx.message.delete()

    @commands.command(pass_context=True, name="warn", aliases=["attention", "achtung"])
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, raison=""):
        """
        Fonction dont le but est d'avertir une personne sur son comportement.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param member: chaine de caractères correspondant au nom du membre.
        :param raison: chaine de caractères correspondant à la raison.

        :return: On a un message du bot avertissant la personne concernée.
        """
        e = discord.Embed(
            title=f"{member} vous avez un avertissement, attention à vous !",
            description=f"Raison : `{raison}`",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=e)

    async def createMutedRole(self, ctx):
        """
        Fonction qui créer un rôle Muted une commande mute a été utilisée manuellement par un modérateur.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...

        :return: rôle créé si fonction active.
        """
        mutedRole = await ctx.guild.create_role(name="Muted",
                                                permissions=discord.Permissions(send_messages=False, speak=False),
                                                read_message_history=True, read_messages=True,
                                                reason="Creation du role Muted pour mute des gens.")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, send_messages=False, speak=False, read_message_history=True,
                                          read_messages=True)
        return mutedRole

    async def getMutedRole(self, ctx):
        """
        Fonction qui affecte le rôle Muted à la personne concernée.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...

        :return: la personne reçoit le rôle Muted.
        """
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Muted":
                return role
        return await self.createMutedRole(ctx)

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
        """
        Cette fonction permet de mute une personne, c'est-à-dire qu'elle est toujours dessus mais qu'elle ne peut
        pas intéragir avec les channels et écrire des messages.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param member: chaine de caractères correspondant au nom du membre.
        :param reason: chaine de caractères correspondant à la raison.

        :return: On a un message du bot attestant du mute de la personne.
        """
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
        """
        Cette fonction est l'inverse de la fonction mute. C'est-à-dire qu'elle peut de nouveau accéder à tout le serveur.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param member: chaine de caractères correspondant au nom du membre.
        :param reason: chaine de caractères correspondant à la raison.

        :return: On a un message du bot attestant du demute de la personne.
        """
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

    @commands.command(pass_context=True, name="slowmode", aliases=["lent"])
    @commands.has_permissions(administrator=True)
    async def slowmode(self, ctx, seconds: int):
        """
        Fonction qui permet de restreindre les messages dans un channel pendant le nombre de secondes souhaitées.

        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param seconds: integer concernant le nombre de secondes que l'on souhaite

        :return:On obtient un message de vérification du bot et le channel n'est plus accessible pendant le nombre de secondes choisies.
        """
        await ctx.channel.edit(slowmode_delay=seconds)
        e = discord.Embed(
            title=f"Le slowmode a été activé pour {seconds} secondes!",
            color=0xff0000
        )
        e.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Moderation(client))
