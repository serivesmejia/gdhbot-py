import discord
import datetime

import os

from screenshot_saturday import ScreenshotSaturday
import asyncio

client = discord.Client()

database = 0

def start(db, discord_token):
    global database
    database = db
    client.run(discord_token); #start bot execution

@client.event
async def on_ready():
    print('Logged in as {0}!'.format(client.user))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Game Dev | !ayuda"))  
    client.loop.create_task(ssaturday_task())

async def ssaturday_task():
    s_saturday = ScreenshotSaturday(client, database, "@everyone Es sabado! <#602995522407497779> esta activado, compartan los avances de sus proyectos ahi <:stonks:631841741212876831>")
    while True:
        await s_saturday.check_ss()
        await asyncio.sleep(30)

@client.event
async def on_message(message):
    if(message.content == "!purga"):
      if(discord.utils.get(message.author.roles, name="Bot Master") is None):
        await message.channel.send(message.author.mention + ", no tienes permiso para ejecutar el comando")
      else:
        await message.channel.send("Iniciando purga de miembros inactivos... (Con el rol 'Nuevo' y mas de una semana en el server)")
        counter = 0
        for member in message.guild.members:
            if(not (discord.utils.get(member.roles, name="Nuevo") is None)):
              if((member.joined_at - datetime.datetime.now()).days < 7):
                await member.send("Has sido expulsado de Game Dev Hispano por inactividad. Si deseas volver a entrar, puedes volver a usar el link de invitacion: https://discord.gg/xRpqqms")
                await message.guild.kick(member, reason="Inactividad")
                counter += 1
        await message.channel.send("Purga finalizada, t otal: " + str(counter))
    elif(message.content == "!alive"):
      await message.delete()
      await message.channel.send(message.author.mention + ", aqui estoy!")
    elif(message.content == "!kill"):
      if(discord.utils.get(message.author.roles, name="Bot Master") is None):
        await message.delete()
        await message.channel.send(message.author.mention + " no tienes permiso para ejecutar el comando")
      else:
        await message.channel.send(message.author.mention + ", el proceso terminara ahora (exit code 0)")
        os._exit(0)