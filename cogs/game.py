import discord
import os
import platform
import random
from discord.ext import commands

class Games(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command(name="gtesting")
  async def gtesting(self, ctx):
    await ctx.send(f"Testing Completed!!")

def setup(bot):
  bot.add_cog(Games(bot))