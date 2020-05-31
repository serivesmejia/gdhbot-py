import bot
import os

discord_token = os.getenv("discord_token") #get bot token from .env file

gdhBot = bot.GDHBotClient #initialize bot client instance
gdhBot.run(discord_token); #start bot execution