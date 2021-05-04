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
        if ctx.message.author.guild_permissions.administrator:
            channel = member.guild.system_channel
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="Member Kicked!", description=f"{member.mention} has been kicked from the server!", color=0xF)
            await channel.send(embed=embed)
        else:
            await ctx.send("You are not an admin or moderator. Nice try!")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            channel = member.guild.system_channel
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Member Banned!", description=f"{member.mention} has been banned from the server!", color=0xF)
            await channel.send(embed=embed)
        else:
            await ctx.send("You are not an admin or moderator. Nice try!")

    @commands.command()
    async def unban(self, ctx, *, member):
        if ctx.message.author.guild_permissions.administrator:
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
        else:
            await ctx.send("You are not an admin or moderator. Nice try!")

    @commands.command()
    async def mute(self, ctx, member: discord.Member, reason=None):

        if ctx.message.author.guild_permissions.administrator:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if role not in ctx.guild.roles:
                perms = discord.Permissions(
                    view_channel=True, send_messages=False, speak=False)
                await ctx.guild.create_role(name="Muted", permissions=perms)

            await member.add_roles(role)
            await ctx.send(f'{member.mention} was muted!')
        else:
            await ctx.send("You are not an admin or moderator. Nice try!")


def setup(client):
    client.add_cog(Moderator(client))
