import bot
import server
import os
from sheets_database import SheetsDatabase

server = server.GDHKeepAliveServer() #keep alive http server
server.asyncStart()

database = SheetsDatabase("Server Database")

print(database.get_worksheet_dict(0))

discord_token = os.getenv("discord_token") #get bot token from .env file

gdhBot = bot.GDHBotClient() #initialize bot client instance
gdhBot.run(discord_token); #start bot execution