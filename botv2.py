# bot.py

import os
import sys
import subprocess
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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my.help"), status=discord.Status.online)
    
    p = subprocess.Popen([sys.executable, './time.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    author = message.author.mention
    author2 = str(message.author)
    print(author2)

    messagecontent = message.content.lower()
    print("Message Content: " + message.content)

    if "mensatime" in messagecontent:
        checkarray = mensatime.check(messagecontent)

        if checkarray[0] == 0:
            await message.channel.send(f"{author} Deine Mensazeit ist {usertime.userread(author2)}")
        elif checkarray[0] == 1:
            embedxslist = discord.Embed(title="Folgende Mensazeiten sind eingetragen:\n", description=usertime.userreadall(), color = 0x9998ff)
            await message.channel.send(f"{author} Folgende Mensazeiten sind eingetragen:\n```\n{usertime.userreadall()}\n```")
            #await message.channel.send(embed = embedxslist)
        elif checkarray[0] == 2:
            usertime.userwrite(author2, 'False')
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
            await message.channel.send(f"{author} Deine Zeit ({checkarray[2]} Uhr) wurde eingetragen.")
        elif checkarray[0] == 8:
            usertime.userwrite(author2, checkarray[1])
            await message.channel.send(f"{author} Deine Zeit ({checkarray[2]}:{checkarray[3]}) wurde eingetragen.")
    
    if "my.mensatime.help" == messagecontent or "my.help" == messagecontent:
        description = "Der Bot unterstützt folgende Befehle:\n**my.help** oder **my.mensatime.help** - trivial.\n**my.mensatime**\n> ohne weiteren Command gibt er euch eure Zeit zurück.\n> = HH:MM oder HH Uhr oder HH:MM Uhr - geht alles.\n> **False** - wird später bei xs.mensatime wichtig.\nxs.mensatime\n> Gibt euch eine Liste zurück von Mensazeiten der User, die sich eingetragen haben.\n> Insofern ihr bei my.mensatime = False eingegeben habt, werdet ihr in der xs Liste nicht aufgelistet.\n> Ihr müsst aber um euch wieder einzutragen, einfach euch eine neue Uhrzeit setzen."
        embed = discord.Embed(title="MensaBot Help", description=description,color=0x9998ff)
        await message.channel.send(embed = embed)

#BOT >>RUN
bot.run(TOKEN)