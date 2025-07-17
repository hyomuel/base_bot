import discord, os
from config import *
from discord.ext import commands

class Hyomuel_Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix=commands.when_mentioned_or("뭉개야 "), intents=discord.Intents.all()) # 맨션과 "뭉개야 "를 모두 prefix로 사용한다

	async def on_ready(self):
		print(f"> {self.user} 로그인")


bot = Hyomuel_Bot()
bot.run(token)
