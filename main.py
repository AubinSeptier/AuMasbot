import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")


class AumasBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"{self.user.display.name} est prêt !")


#aumas_bot = AumasBot
#AumasBot.run(os.getenv("TOKEN"))
AumasBot.run("OTcwNjgyODE4MDM4NDg5MTI5.GG67vG.xuCNUm8DV0Jtxs7nMQftH7Ud_BL-EgugURhRm4")