# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

#IMPORTS Discord..............END
import usertime
import mensatime
#IMPORTS......................END

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = "",intents=intents)

#BOTEVENTS


        
    

@bot.event
async def on_ready():
    print("Im Ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    author = message.author.mention
    messagecontent = message.content.lower()
    print("Message Content: " + message.content)


    

#BOT >>RUN
bot.run(TOKEN)
