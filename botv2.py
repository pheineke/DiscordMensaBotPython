# bot.py

import asyncio
import os
import sys
import subprocess
import discord
from discord.ext import commands
from discord.ext import tasks

from dotenv import load_dotenv

from datetime import datetime

#IMPORTS Discord..............END
import usertime
import mensatime
import helpmessage
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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my.help"), status=discord.Status.online)
    bot.loop.create_task(my_task())

@bot.event
async def on_message(message):
    if message.author.bot and message.author.bot == "N1ghts Little Helper#2772":
        return

    author = message.author.mention
    #print(author)
    author2 = str(message.author)
    #print(author2)

    messagecontent = message.content.lower()
    #print("Message Content: " + message.content)

    if "mensatime" in messagecontent:
        # Erwähnten Benutzer abrufen
        if message.mentions:
            member = message.mentions[0]
            username = member.name

        

        checkarray = mensatime.check(messagecontent)

        if checkarray[0] == 0:
            await message.channel.send(f"{author} Deine Mensazeit ist {usertime.userread(author2)}")
        elif checkarray[0] == 1:
            #embedxslist = discord.Embed(title="Folgende Mensazeiten sind eingetragen:\n", description=usertime.userreadall(), color = 0x9998ff)
            await message.channel.send(f"{author} Folgende Mensazeiten sind eingetragen:\n```\n{usertime.userreadall()}\n```")
            #await message.channel.send(embed = embedxslist)
        elif checkarray[0] == 2:
            usertime.userwrite(author2, 'false')
            await message.channel.send(f"{author} Usertime wurde disabled.")
        elif checkarray[0] == 3:
            await message.channel.send(f"{author} Um deine Usertime zu enablen setze deine Mensatime auf eine neue Uhrzeit.")
        elif checkarray[0] == 4:
            if checkarray[1] == 'const':
                usertime.setuserconst(author2)
                await message.channel.send(f"{author} Deine Usertime wurde als konstant vermerkt.")
            elif checkarray[1] == 'nconst':
                usertime.deluserconst(author2)
                await message.channel.send(f"{author} Deine Usertime wurde als nicht-konstant eingetragen.") 
        elif checkarray[0] == 5:
            await message.channel.send(f"{author} {usertime.userdelete()}") 
        elif checkarray[0] == 6:
            await message.channel.send(f"{author} Deine Eingabe war ungültig.")
        elif checkarray[0] == 7:
            usertime.userwrite(author2, checkarray[1])
            await message.channel.send(f"{author} Deine Zeit ({checkarray[2]}:{checkarray[3]} Uhr) wurde eingetragen.")
        elif checkarray[0] == 8:
            membername = username
            #print(membername)
            await message.channel.send(f"{author} Die Zeit von {checkarray[1]} wurde {usertime.userwriteuser(author2, membername)}")
    
    if "my.mensatime.help" == messagecontent or "my.help" == messagecontent:
        embed = discord.Embed(title="MensaBot Help", description=helpmessage.help(),color=0x9998ff)
        await message.channel.send(embed = embed)
    

    ## ADMIN COMMANDS
    if "admin:xs:userreset" == messagecontent and author2 == "r4ge_6168":
        usertime.userreset()
        await message.channel.send("###userreset done")
    if "admin:userdelete" in messagecontent and author2 == "r4ge_6168":
        try:
            string = messagecontent.split(":")
            print(string)
        except:
            await message.channel.send("###userdel cmd falsch (admin:userdelete:username:yes)")
        else:
            if string[3] == "yes":
                returnstring = usertime.userdelete(string[2])
            await message.channel.send(returnstring)


async def my_task():
    while True:
        currenttime = str(datetime.now().strftime("%H:%M"))
        if currenttime == "15:00":
           usertime.userreset()
        await asyncio.sleep(30)

#BOT >>RUN
bot.run(TOKEN)