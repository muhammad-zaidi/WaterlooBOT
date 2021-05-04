import discord
from discord.ext import commands
import random


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("misc.py is ready")

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Latency Check ⏰", description=f'Your ping is {round(self.client.latency * 1000)}ms!', color=0xFF0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def waterloo(self, ctx):
        await ctx.send("WATER WATER WATER")
        await ctx.send("LOO LOO LOO")

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()

        await ctx.send(message)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(
            color=ctx.author.color)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Misc(client))
