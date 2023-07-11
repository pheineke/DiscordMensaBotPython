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

    if "mensatime" in messagecontent:
        checkarray = mensatime.check(messagecontent)

        if checkarray[0] == 0:
            await message.channel.send(f"{author} Deine Mensazeit ist: {usertime.userread(author)}")
        elif checkarray[0] == 1:
            await message.channel.send(f"{author} Folgende Mensazeiten sind eingetragen:\n {usertime.userreadall()}")
        elif checkarray[0] == 2:
            usertime.userwrite(author, 'False')
            await message.channel.send(f"{author} Usertime wurde disabled.")
        elif checkarray[0] == 3:
            await message.channel.send(f"{author} Um deine Usertime zu enablen setze deine Mensatime auf eine neue Uhrzeit.")
        elif checkarray[0] == 4:
            await message.channel.send(f"{author} Deine Eingabe war ungültig.")
        elif checkarray[0] == 5:
            usertime.userwrite(author, checkarray[1])
            
            await message.channel.send(f"{author} Deine Zeit ({checkarray[2]} Uhr) wurde eingetragen.")
        elif checkarray[0] == 6:
            usertime.userwrite(author, checkarray[1])
            
            await message.channel.send(f"{author} Deine Zeit ({checkarray[2]}:{checkarray[3]}) wurde eingetragen.")
       

    


    

#BOT >>RUN
bot.run(TOKEN)
