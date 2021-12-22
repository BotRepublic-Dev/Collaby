import discord
from discord.interactions import Interaction
import dotenv
import random
import platform
from time import time
from discord.ext import commands
from discord.ext.commands.cooldowns import C
from discord.components import Button, SelectOption
from discord.ext.commands.core import command
from discord.ui import Button, View, Select
from discord.ui.button import button
from os import scandir
import os

class Games(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command(name="gtesting")
  async def gtesting(self, ctx):
    await ctx.send(f"Testing Completed!!")

  @commands.command()
  async def gamenight(self, ctx,  url=None, *,  game):
      await ctx.defer()
      if not url is None:
          button = Button(label="Join game!", style=discord.ButtonStyle.green, emoji="🎮" , url=url)
      view = View()
      if not url is None:
          view.add_item(button)
      await ctx.send(f"GAME NIGHT! Game: {game}", view=view)

def setup(bot):
  bot.add_cog(Games(bot))