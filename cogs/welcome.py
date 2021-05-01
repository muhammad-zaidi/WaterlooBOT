import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("welcome.py is ready")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        embed = discord.Embed(
            title="Welcome!", description=f"{member.mention} joined the server!", color=0x00ff00)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Welcome(client))
