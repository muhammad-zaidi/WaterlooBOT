import discord
from discord.ext import commands
from translate import Translator


class translation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("translation.py is ready")

    @commands.command()
    async def translate(self, ctx):
        await ctx.send("test")


def setup(client):
    client.add_cog(translation(client))
