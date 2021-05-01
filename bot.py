import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)


def token():
    with open("WaterlooBOT/token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = token()


@client.event
async def on_ready():
    print("Bot.py has started.")


for filename in os.listdir("WaterlooBOT/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)
