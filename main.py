import bot
import server
import os
import encryption
from sheets_database import SheetsDatabase

server.GDHKeepAliveServer().asyncStart() #keep alive http server

decrypt_key = os.getenv("decrypt_key")

decrypted_client_secret = encryption.decrypt_str(os.getenv("client_secret_fernet"), decrypt_key)

database = SheetsDatabase("Server DataBase", "1-uyTYXpOHNWEMlOXHxfVD8LU_UGgIw2wiheAoddVxVk", decrypted_client_secret)

discord_token = os.getenv("discord_token") #get bot token from .env file

bot.start(database, discord_token) #initialize bot client instance