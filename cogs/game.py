import random
from random import randint

import discord
from discord.ext import commands


class Game(commands.Cog):
    def __init__(self, client):
        """
        La fonction __init__ est appelé à chaque fois qu'un objet est créé à partir d'une classe. La fonction sert à
        initialiser les attributs de l'objet.

        :param self : ce paramètre est utilisé pour représenter l'instance de la classe. On peut donc grâce à lui
        accéder aux attributs et aux méthodes de la classe
        :param client: il définit notre BOT définit dans la main mais ici on l'initie aussi dans la classe.
        """
        self.client = client

        self.player1 = ""
        self.player2 = ""
        self.turn = ""
        self.gameOver = True
        self.count = 0
        self.board = []

        self.winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

    @commands.command(pass_context=True, aliases=["morpion", "morp"])
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):

        """
        La fonction tictactoe + <nomjoueur1> + <nomjoueur2> permet de lancer un partie de morpion dans le salon où la
        commande a été appelée.

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été
        rentrée.Par exemple le salon Discord, la personne qui a appelée la fonction etc...

        :param p1: chaine de caractères qui correspond au nom du joueur 1
        :param p2: chaine de caractères qui correspond au nom du joueur 2

        :return: en retour on obtient le lancement du jeu
        """

        if self.gameOver:
            self.board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                          ":white_large_square:", ":white_large_square:", ":white_large_square:",
                          ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            self.turn = ""
            self.gameOver = False
            self.count = 0

            self.player1 = p1
            self.player2 = p2

            # affiche le tableau
            line = ""
            for x in range(len(self.board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + self.board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + self.board[x]

            # determine quel joueur joue en premier
            num = randint(1, 2)
            if num == 1:
                self.turn = self.player1
                morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                             description=f"<@" + str(self.player1.id) + "> commence la partie !",
                                             color=0x0080ff)
                await ctx.send(embed=morpionEmbed)
            elif num == 2:
                self.turn = self.player2
                morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                             description=f"<@" + str(self.player2.id) + "> commence la partie !",
                                             color=0x0080ff)
                await ctx.send(embed=morpionEmbed)
        else:
            morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                         description=f"Une partie est déjà en cours, finissez la avant d'en commencer une autre.",
                                         color=0x0080ff)
            morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=morpionEmbed)

    @commands.command(pass_context=True, aliases=["p", "places"])
    async def place(self, ctx, pos: int):
        """
        La fonction place + <numéro_de_la_case> permet de placer son signe dans la case souhaitée

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param pos: représente un nombre qui correspond au numéro de la case sur le plateau du morpion

        :return: le pion du joueur se place sur la case choisi
        """

        if not self.gameOver:
            mark = ""
            if self.turn == ctx.author:
                if self.turn == self.player1:
                    mark = ":regional_indicator_x:"
                elif self.turn == self.player2:
                    mark = ":o2:"
                if 0 < pos < 10 and self.board[pos - 1] == ":white_large_square:":
                    self.board[pos - 1] = mark
                    self.count += 1

                    # affiche le tableau
                    line = ""
                    for x in range(len(self.board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + self.board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + self.board[x]

                    self.checkWinner(self.winningConditions, mark)
                    print(self.count)
                    if self.gameOver is True:
                        morpionEmbed = discord.Embed(title=f"Résultat du morpion !",
                                                     description=mark + " wins!",
                                                     color=0x0080ff)
                        await ctx.message.delete()
                        await ctx.send(embed=morpionEmbed)
                    elif self.count >= 9:
                        self.gameOver = True
                        morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                                     description=f"C'est une égalité !",
                                                     color=0x0080ff)
                        await ctx.send(embed=morpionEmbed)

                    # changement de tours
                    if self.turn == self.player1:
                        self.turn = self.player2
                    elif self.turn == self.player2:
                        self.turn = self.player1
                else:
                    morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                                 description=f"Assurez-vous de rentrer un entier allant de 1 à 9, et de choisir une case pas complète !",
                                                 color=0x0080ff)
                    morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=morpionEmbed)

            else:
                morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                             description=f"Ce n'est pas votre tour. Attendez patiemment !",
                                             color=0x0080ff)
                morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.message.delete()
                await ctx.send(embed=morpionEmbed)

        else:
            morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                         description=f"Vous pouvez relancer une partie avec la commande !tictactoe.",
                                         color=0x0080ff)
            await ctx.message.delete()
            await ctx.send(embed=morpionEmbed)

    # condition pour gagner
    def checkWinner(self, winningConditions, mark):
        """
        Cette fonction permert de voir en permanence si un joueur a gagné ou si la partie est terminée. Cette fonction
        n'est pas censé être appelée.

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param winningConditions: représente les conditions de victoire d'un joueur, représentées par un tableau.
        :param mark: chaine de caractère (ici signe) qui est active lorsqu'un joueur place un pion dans une case.

        :return: en retour on obtient une boucle qui vérifie si un joueur a gagné ou si la partie est terminée.
        """

        for condition in self.winningConditions:
            if self.board[condition[0]] == mark and self.board[condition[1]] == mark and self.board[
                condition[2]] == mark:
                self.gameOver = True

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        """
        La fonction tictactoe_error permet au BOT de vérifier s'il y a pas eu d'erreur lors de l'appel de la fonction.

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param error: paramètre représentant des conditions possible d'erreurs lors de l'appel de la fonction.

        :return: on obtient un message du BOT qui dit quelle erreur on a pu faire.
        """
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                         description=f"N'oubliez pas de mentionner 2 personnes",
                                         color=0x0080ff)
            morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=morpionEmbed)
        elif isinstance(error, commands.BadArgument):
            morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                         description=f"Assurez-vous de mentionner un membre du serveur "
                                                     f"(exemple <@970682818038489129>).",
                                         color=0x0080ff)
            morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=morpionEmbed)

    @place.error
    async def place_error(self, ctx, error):
        """
        Fonction qui permet au bot de dire où est ce qu'on a pu se tromper lors du placment d'un pion.

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param error: paramètre représentant des conditions possible d'erreurs lors de l'appel de la fonction.

        :return: on obtient un message du BOT qui dit quelle erreur on a pu faire.
        """
        if isinstance(error, commands.MissingRequiredArgument):
            morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                         description=f"Entrez la position que vous souhaitez marquer.",
                                         color=0x0080ff)
            morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=morpionEmbed)
        elif isinstance(error, commands.BadArgument):
            morpionEmbed = discord.Embed(title=f"Jeu du morpion !",
                                         description=f"Rentrez un entier s'il vous plait !",
                                         color=0x0080ff)
            morpionEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=morpionEmbed)

    @commands.command(pass_context=True, aliases=["pfc"])
    async def rps(self, ctx, message):
        """
        La fonction rps permet de lancer une partie de "pierre feuille ciseaux" contre le BOT.

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param message: chaine de caractères représentant le choix de celui qui appelle la commande.

        :return: On obtient l'affichage du résultat de la partie ou les erreurs rencontrées lors de l'appel de la fonction.
        """
        answer = message.lower()
        choices = ["pierre", "feuille", "ciseaux"]
        computers_answer = random.choice(choices)
        if answer not in choices:
            rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                     description=f"L'option choisi n'est pas possible. Choisissez entre : pierre, "
                                                 f"feuille ou ciseaux !", color=0x0080ff)
            rpsEmbed.set_footer(text=f"Ce message concerne {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.message.delete()
            await ctx.send(embed=rpsEmbed)
        else:
            if computers_answer == answer:
                rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                         description=f"Égalité ! Nous sommes tous les deux tombés sur {answer} "
                                                     f"\U0001F62E",
                                         color=0x0080ff)
                rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.message.delete()
                await ctx.send(embed=rpsEmbed)
            if computers_answer == "pierre":
                if answer == "feuille":
                    rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                             description=f"Tu as gagné ! J'ai choisi \U0001FAA8 "
                                                         f"et tu as pris \U0001F4C4. Bien joué ! \U0001F44F",
                                             color=0x0080ff)
                    rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=rpsEmbed)
                if answer == "ciseaux":
                    rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                             description=f"J'ai gagné ! J'ai choisi \U0001FAA8 "
                                                         f"et tu as pris \U00002702. Essaie encore ! \U0001F609	",
                                             color=0x0080ff)
                    rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=rpsEmbed)

            if computers_answer == "feuille":
                if answer == "ciseaux":
                    rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                             description=f"Tu as gagné ! J'ai choisi \U0001F4C4 "
                                                         f"et tu as pris \U00002702. Bien joué ! \U0001F44F",
                                             color=0x0080ff)
                    rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=rpsEmbed)
                if answer == "pierre":
                    rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                             description=f"J'ai gagné ! J'ai choisi \U0001F4C4 "
                                                         f"et tu as pris \U0001FAA8. Essaie encore ! \U0001F609",
                                             color=0x0080ff)
                    rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=rpsEmbed)

            if computers_answer == "ciseaux":
                if answer == "pierre":
                    rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                             description=f"Tu as gagné ! J'ai choisi \U00002702 "
                                                         f"et tu as pris \U0001FAA8. Bien joué ! \U0001F44F ",
                                             color=0x0080ff)
                    rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=rpsEmbed)
                if answer == "feuille":
                    rpsEmbed = discord.Embed(title=f"Pierre feuille ciseaux !",
                                             description=f"J'ai gagné ! J'ai choisi \U00002702 "
                                                         f"et tu as pris \U0001F4C4. Essaie encore ! \U0001F609",
                                             color=0x0080ff)
                    rpsEmbed.set_footer(text=f"Jeu lancé par {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.message.delete()
                    await ctx.send(embed=rpsEmbed)

    @commands.command(pass_context=True, aliases=["dices", "dés", "dé"])
    async def dice(self, ctx, nombre: int):
        """
        La fonction dice + <nombre> permet à celui qui écrit la commande de lancer un dé de son choix.

        :param self: représente l'objet cible, c'est à dire qu'il réfère à l'objet qui est en cours de création.
        On pourra donc accéder aux fonctionnalités de cet objet.
        :param ctx: permet d'obtenir des informations par rapport à l'environnement dans lequel la commande a été rentrée.
        Par exemple le salon Discord, la personne qui a appelée la fonction etc...
        :param nombre: permet de rentrer un nombre pour avoir le nombre de faces souhaitées

        :return : en retour on obtient le résultat de la face sur laquelle le dé est tombé.
        """
        result = randint(1, nombre)  # Prend un nombre aléatoire entre 1 et nombre
        diceEmbed = discord.Embed(title=f"Tirage d'un dé de {nombre} !", description=f"Le dé est tombé sur {result} !",
                                  color=0x0080ff)
        diceEmbed.set_footer(text=f"Tirage effectué par {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=diceEmbed)


def setup(client):
    client.add_cog(Game(client))
