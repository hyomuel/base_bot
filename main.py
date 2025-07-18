import discord, os
from config import *
from discord.ext import commands

class Hyomuel_Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix=commands.when_mentioned_or("뭉개야 "), intents=discord.Intents.all()) # 맨션과 "뭉개야 "를 모두 prefix로 사용한다

	async def on_ready(self):
		print(f"> {self.user} 로그인")

def remove_pycache(target_dir): # __pycache__가 있는게 너무 신경쓰여서 만든 함수
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))
    print("> 캐시 삭제 완료")


bot = Hyomuel_Bot()

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        if file.startswith("_"):
            continue
        bot.load_extension(f"cogs.{file[:-3]}") # cogs 폴더에서 파일 이름 앞에 _가 없을 경우에만 적용시키기

remove_pycache("./")
bot.run(token)

