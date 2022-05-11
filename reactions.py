import discord

client = discord.Client()

@client.event
async def on_message(message):

    if message.content.lower() == "quoi":
        await message.channel.send("feur")

    if message.content.lower() == "oui":
        await message.channel.send("stiti")

    if message.content.lower() == "wesh":
        await message.channel.send("dene")

    if message.content.lower() == "ouai":
        await message.channel.send("stern")

    if message.content.lower() == "comment":
        await message.channel.send("aire")

    if message.content.lower() == "non":
        await message.channel.send("bril")

    if message.content.lower() == "ping":
        await message.channel.send("pong")

    if message.content() == "Je suis trop fort":
        await message.channel.send("Oui c'est ça")