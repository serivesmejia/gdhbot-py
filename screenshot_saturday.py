import datetime
import discord

class ScreenshotSaturday:

    def __init__(self, bot, database, message_ss):
        self.bot = bot
        self.database = database
        self.message_ss = message_ss

        self.guild = bot.get_guild(573233534752522285)
        self.channel = self.guild.get_channel(573233547477909521)

    async def check_ss(self):

        today = datetime.datetime.today()

        if(today.weekday() == 5):
            await self.do_saturday(today)
        else:
            await self.do_notsaturday()

    async def do_saturday(self, today):
        df = self.database.get_worksheet_dataframe("keynvalue", False)

        today_str = today.strftime("%Y %m %d")

        if(df.at[0,1] != today_str):
            self.database.change_value_push("keynvalue", 0, 1, today_str, True)
            
            await self.channel.send(self.message_ss)

        await self.guild.get_channel(602995522407497779).set_permissions(discord.utils.get(self.guild.roles, id=587356766258331653), send_messages=True)

    async def do_notsaturday(self):
        await self.guild.get_channel(602995522407497779).set_permissions(discord.utils.get(self.guild.roles, id=587356766258331653), send_messages=False)