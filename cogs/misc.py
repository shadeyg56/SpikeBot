import discord
from ext.commands import Bot
from discord.ext import commands
import datetime
import time
import pykemon

class Misc():
    
  def __init__(self, bot):
      self.bot = bot
        
  poke = pykemon.V1Client()
        
  async def send_cmd_help(self,ctx):
      if ctx.invoked_subcommand:
          pages = self.bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
          for page in pages:
              await self.bot.send_message(ctx.message.channel, page)
      else:
          pages = self.bot.formatter.format_help_for(ctx, ctx.command)
          for page in pages:
              await self.bot.send_message(ctx.message.channel, page)
     
    
  @commands.command(pass_context = True)
  async def ping(self,ctx):
      msgtime = ctx.message.timestamp.now()
      await (await self.bot.ws.ping())
      now = datetime.datetime.now()
      ping = now - msgtime
      pong = discord.Embed(title='Pong! Response Time:', description=str(ping.microseconds / 1000.0) + ' ms',
                          color=FF3DFE)
      await self.bot.send_message(ctx.message.channel, embed=pong)
      await self.bot.add_reaction(pong, '\U0001f3d3')
    
  @commands.command(pass_context = True)
  async def say(self,ctx, message: str):
      '''Say something as the bot'''
      await self.bot.say(message)
      await self.bot.delete_message(ctx.message)
    
  @commands.command(pass_context = True)
  async def pokemon(self, ctx):
      test = poke.get_pokemon(uid=1)
      self.bot.say('test')
      
        
        

def setup(bot):
    bot.add_cog(Misc(bot))

