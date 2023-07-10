# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

#IMPORTS Discord..............END
import usertime
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

    messagecontent = message.content.lower()
    print("Message Content: " + message.content)


    if 'my.' in messagecontent:

        author = message.author.mention
        print(author)

        if 'mensatime' in messagecontent:
            if ".del" in messagecontent:
                try:
                    usertime.userdelete(author)
                except:
                    await message.channel.send("Dieser User ist nicht vorhanden.")
                else:
                    await message.channel.send("Dein Eintrag wurde gelöscht.")

            elif '=' in messagecontent:
                try:
                    uhrzeitsplitstring = messagecontent.split()[2].split(':')
                except:
                    await message.channel.send("Das ist keine gültige Uhrzeit.\nUhrzeiten werden folgendermaßen angegeben: HH:MM")

                else:
                    #await message.channel.send(uhrzeitsplitstring)

                    try:
                        uhrzeitsplitintcheck = [int(uhrzeitsplitstring[0])] + [int(uhrzeitsplitstring[1])]
                    except:
                        await message.channel.send("Das ist keine gültige Uhrzeit.\nUhrzeiten werden folgendermaßen angegeben: HH:MM")

                    else:
                        if (0 <= uhrzeitsplitintcheck[0] <= 24) and (0 <= uhrzeitsplitintcheck[1] <= 59):
                                timestringmil = int("".join(uhrzeitsplitstring))

                                #await message.channel.send(uhrzeitsplitstring)
                                #await message.channel.send(timestringmil) 
                                usertime.userwrite(author, timestringmil)

                                await message.channel.send(str(author) + " deine Mensatime wurde auf " + usertime.userread(author) + "gestellt.")

                        else: await message.channel.send("Das ist keine gültige Uhrzeit.\nUhrzeiten werden folgendermaßen angegeben: HH:MM")
            elif 'None' in messagecontent:
                
            else:
                try:
                    userread = usertime.userread(author)
                except:
                    await message.channel.send("Der User hat keinen Eintrag.")
                else:
                    await message.channel.send("Deine Uhrzeit beträgt " + str(userread))
            
        else:
            await message.channel.send("Du hast leider keinen gültigen Befehl eingegeben." + str(message.author.mention))
    elif "xs.mensatime" in messagecontent: 
        await message.channel.send("Mensazeiten für eingetragene User")
        await message.channel.send(usertime.userreadall())

#BOT >>RUN
bot.run(TOKEN)