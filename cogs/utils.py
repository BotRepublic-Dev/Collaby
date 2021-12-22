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


class Utils(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command(name="ping")
  async def ping(self,ctx):
    api_start = time()
    msg = await ctx.send("Ping...")
    api_end = time()
    button = Button(label="Invite me!", style=discord.ButtonStyle.green, emoji="<:collaby:921854424224268298>" , url="http://collabyinv.itzfinleyplayz.org")
    view = View()
    view.add_item(button)
    em = discord.Embed(title="Pong! :ping_pong: ", color=discord.Color.green())
    em.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms ")
    em.add_field(name="API", value=f"{str(round((api_end - api_start) * 1000))}ms ")
    em.set_footer(text="Collaby! By Bot Republic")
    await ctx.send(embed = em, view=view)




def setup(bot):
  bot.add_cog(Utils(bot))