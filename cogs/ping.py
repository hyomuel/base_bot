import discord, time, platform, psutil
from discord.ext import commands

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name="ping", description="봇의 지연시간을 확인합니다")
    async def ping(self, ctx):
        """봇의 지연시간을 확인합니다"""
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"지연시간: **{round(self.bot.latency * 1000)}ms**",
            color=0x00ff00
        )
        await ctx.reply(embed=embed)

    @commands.slash_command(name="ping", description="봇의 지연시간을 확인합니다")
    async def ping(self, ctx):
        """봇의 지연시간을 확인합니다"""
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"지연시간: **{round(self.bot.latency * 1000)}ms**",
            color=0x00ff00
        )
        await ctx.respond(embed=embed)

    @commands.slash_command(name="info", description="봇 정보를 표시합니다")
    async def info(self, ctx):
        """봇 정보를 표시합니다"""
        uptime = time.time() - self.start_time
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        embed = discord.Embed(
            title="🤖 봇 정보",
            description="파이썬으로 제작된 디스코드 봇입니다",
            color=0x00ff00
        )
        embed.add_field(name="서버 수", value=f"{len(self.bot.guilds)}개", inline=True)
        embed.add_field(name="지연시간", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="업타임", value=f"{int(hours)}시간 {int(minutes)}분", inline=True)
        embed.add_field(name="파이썬 버전", value=platform.python_version(), inline=True)
        embed.add_field(name="discord 모듈 버전", value=discord.__version__, inline=True)
        embed.add_field(name="CPU 사용률", value=f"{psutil.cpu_percent()}%", inline=True)
        
        await ctx.respond(embed=embed)

    @commands.slash_command(name="server", description="서버 정보를 표시합니다")
    async def server(self, ctx):
        """서버 정보를 표시합니다"""
        guild = ctx.guild
        
        embed = discord.Embed(
            title=f"📊 {guild.name} 정보",
            color=0x00ff00
        )
        embed.add_field(name="서버 ID", value=guild.id, inline=True)
        embed.add_field(name="소유자", value=guild.owner.mention, inline=True)
        embed.add_field(name="생성일", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="멤버 수", value=guild.member_count, inline=True)
        embed.add_field(name="채널 수", value=len(guild.channels), inline=True)
        embed.add_field(name="역할 수", value=len(guild.roles), inline=True)
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        await ctx.respond(embed=embed)

    @commands.slash_command(name="user", description="사용자 정보를 표시합니다")
    async def user(self, ctx, member: discord.Member = None):
        """사용자 정보를 표시합니다"""
        if member is None:
            member = ctx.author
            
        embed = discord.Embed(
            title=f"👤 {member.name} 정보",
            color=member.color
        )
        embed.add_field(name="사용자 ID", value=member.id, inline=True)
        embed.add_field(name="계정 생성일", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="서버 참가일", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="최고 역할", value=member.top_role.mention, inline=True)
        embed.add_field(name="봇 여부", value="예" if member.bot else "아니오", inline=True)
        
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        
        await ctx.respond(embed=embed)

    @commands.slash_command(name="help", description="도움말을 표시합니다")
    async def help(self, ctx):
        """도움말을 표시합니다"""
        embed = discord.Embed(
            title="📚 도움말",
            description="사용 가능한 명령어 목록입니다",
            color=0x00ff00
        )
        
        commands_list = [
            ("/ping", "봇의 지연시간을 확인합니다"),
            ("/info", "봇 정보를 표시합니다"),
            ("/server", "서버 정보를 표시합니다"),
            ("/user [사용자]", "사용자 정보를 표시합니다"),
            ("/help", "이 도움말을 표시합니다")
        ]
        
        for cmd, desc in commands_list:
            embed.add_field(name=cmd, value=desc, inline=False)
        
        await ctx.respond(embed=embed)
