from datetime import timedelta
import discord
import os
from discord.ext import commands
from discord.utils import utcnow
class Moderation(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command(name="slowmode")
  @commands.has_permissions(manage_channels=True)
  async def slowmode(self, ctx, length: int):
    await ctx.defer()
    await ctx.channel.edit(slowmode_delay=length)
    await ctx.send(f"Ok boss, set slowmode to ``{length}`` seconds")
    

  @commands.command(name="lockdown")
  @commands.has_permissions(manage_channels=True)
  async def lockdown(self, ctx):
    await ctx.defer()
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send( f"{ctx.channel.mention} ***is now in lockdown.***")

  @commands.command(name="unlock")
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx):
    await ctx.defer()
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
    await ctx.send( f"{ctx.channel.mention} ***is now unlocked.***")

  @commands.command(name="kick")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason = None):
    await ctx.defer()
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked for ``{reason}``")

  @commands.command(name="ban")
  @commands.has_permissions(kick_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason = None):
    await ctx.defer()
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} was banned for ``{reason}``")

  @commands.command(name="ban")
  @commands.has_permissions(kick_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason = None):
    await ctx.defer()
    await member.unban(reason=reason)
    await ctx.send(f"{member.mention} was unbanned for ``{reason}``")

 

def setup(bot):
  bot.add_cog(Moderation(bot))