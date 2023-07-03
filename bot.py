# bot.py
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv
#IMPORTS Discord..............END

#import usertime
import re
import json


#IMPORTS......................END



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix = "+",intents=intents)



@bot.event
async def on_ready():
    print("Im Ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print("Message Content: " + message.content)

    neuevariable = message.content.split()



    if 'My.' in message.content:
        if 'Mensatime' in message.content:
            await message.channel.send(neuevariable)
            await message.channel.send("And the oscar goes to " + str(message.author.mention))
        else:
            await message.channel.send('duhs ist Standort ' + str(message.author.mention))        


        
        #await message.channel.send('du hs')



'''
@bot.command()
async def members(ctx):
    for guild in client.guilds:
        for member in guild.members:
            print(member)

'''

bot.run(TOKEN)