# bot.py
import os
import token
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv(token.token)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token.txt)