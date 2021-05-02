import discord
from discord.ext import commands


class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("moderator.py is ready")

    @commands.command()
    async def kick(self, ctx, member: discord.Member, reason=None):
        channel = member.guild.system_channel
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="Member Kicked!", description=f"{member.mention} has been kicked from the server!", color=0xF)
        await channel.send(embed=embed)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason=None):
        channel = member.guild.system_channel
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="Member Banned!", description=f"{member.mention} has been banned from the server!", color=0xF)
        await channel.send(embed=embed)

    @commands.command()
    async def unban(self, ctx, *, member):
        channel = ctx.guild.system_channel
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for entries in banned_users:
            user = entries.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="Member Unbanned!", description=f'{user.mention} has been unbanned from the server!', color=0xF)
                await channel.send(embed=embed)
                return


def setup(client):
    client.add_cog(Moderator(client))
