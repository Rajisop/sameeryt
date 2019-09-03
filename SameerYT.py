import discord
from discord.ext import commands
import asyncio
 
bot=commands.Bot(command_prefix='D')
 
@bot.event
async def on_ready():
    print('The bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
   
   
bot.run('NjA0MjU5Nzg4NTY1NjQzMjg0.XWj7Vw.9nw8phb1OCbPFyVQdVEBY2kEoVs')