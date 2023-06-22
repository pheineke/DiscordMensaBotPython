# bot.py
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()


client = commands.Bot(command_prefix = "+",intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})\n'
          )
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n  {members}')

client.run(TOKEN)