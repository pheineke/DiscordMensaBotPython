# bot.py
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()


client = commands.Bot(command_prefix = "+",intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



client.run(TOKEN)