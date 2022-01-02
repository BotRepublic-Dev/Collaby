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

class About(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command(name="about")
  async def about(self, ctx):
    button = Button(label="About Me!", style=discord.ButtonStyle.green, emoji="<:collaby:921854424224268298>" , url="https://www.botrepublic.itzfinleyplayz.org/collaby")
    view = View()
    view.add_item(button)
    em = discord.Embed(title="About", color=ctx.author.color, timestamp=datetime.utcnow())
    em.add_field(name="Python version", value=platform.python_version(), inline=True)
    await ctx.send(embed = em, view=view)

  @commands.command(name="abp", alias="botrepublic" , description="About Bot Republic")
  async def abp(self ,ctx):
    button = Button(label="About Bot Republic", style=discord.ButtonStyle.green, emoji="<:botrepublic:923167015395553321>" , url="https://www.botrepublic.itzfinleyplayz.org")
    view = View()
    view.add_item(button)
    em = discord.Embed(title="Bot Republic!", color=ctx.author.color, timestamp=datetime.utcnow())
    em.add_field(name= "About Us!", value="A few unknown bots found an empty land and decided to make it their own. They build servers, communities and a country. Bot Republic was born. Bot Republic was founded on 19/12/21 by ThePolarDeveloper! With The Following Owners/Developers Cobalt and ItzFinleyPlayz!")
    await ctx.send(embed = em, view=view)

  @commands.command()
  async def serverstats(self, ctx):
   em = discord.Embed(title=f"Server Stats For {ctx.guild.name}")
   em.add_field(name = "Users:", value = ctx.guild.member_count, inline = False)
   em.add_field(name = "Channels:", value = ctx.guild.channels, inline = False)
   await ctx.send(embed=em)

def setup(bot):
  bot.add_cog(About(bot))