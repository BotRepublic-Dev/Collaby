import discord
import os
from discord import embeds
from discord.flags import alias_flag_value
from discord.interactions import Interaction
import dotenv
import random
import platform
from time import time
from datetime import datetime
from typing import Union, Optional
from discord.ext import commands
from discord.ext.commands.cooldowns import C
from discord.components import Button, SelectOption
from discord.ext.commands.core import command
from discord.ui import Button, View, Select, view
from discord.ui.button import button
from os import scandir

class Random(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command()
  async def rtesting(self, ctx):
   await ctx.send(f"Testing Completed!!")

  @commands.command()
  async def random(self, ctx):
   button1 = Button(label="Click Me!", style=discord.ButtonStyle.red, emoji=("<:collaby:921854424224268298>"))
   
   async def  button_callback(interaction):
    await interaction.response.send_message("Hi")

   button.callback = button_callback 

   view = View()
   view.add_item(button1)
   await ctx.send(f"I dare you to click one of these buttons!", view=view)

def setup(bot):
  bot.add_cog(Random(bot))