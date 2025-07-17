import discord
from discord.ext import commands

def setup(bot: commands.Bot):
	bot.add_cog(Test(bot))

class Test(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def 테스트(self, ctx:commands.Context):
		await ctx.reply("테스트")

	@commands.slash_commands()
	async def 테스트1(self, ctx:discord.ApplicationContext):
		await ctx.respond("테스트")
		# 또는 await.ctx.response.send_message("테스트")
