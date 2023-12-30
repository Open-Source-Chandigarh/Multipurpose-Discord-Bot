import discord
from discord.ext import commands, tasks
import json
import asyncio
import math
from models.server_rank import server_rank


col = discord.Color.purple()

class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
              
    def level_up(self, user):
        account = server_rank.fetch(user)
        
        if account.Experience >= math.ceil((10 * (account.Level ** 4)) / 2):
            account.Level += 1
            account.save()
            return True
        else:
            return False
        
# * -------------------------------------------------------------------   

    @commands.Cog.listener()
    async def on_message(self, message):
        account = server_rank.fetch(message.author)
        if message.author.id == self.bot.user.id:
            return
            
        xp = 5
        account.Experience += xp
        account.save()
        
        if self.level_up(message.author):
            level_up_embed = discord.Embed( title = "Woohoo - Leveled Up!", color=col)
            level_up_embed.set_author(name = message.author.display_name, icon_url=message.author.display_avatar.url)
            level_up_embed.add_field(name = "Congratulations", value=f"{message.author.mention} has leveled up to level `{account.Level+1}` !")
        
            sent = await message.channel.send(embed = level_up_embed)
            sent
            await asyncio.sleep(10)
            await sent.delete()

# * -------------------------------------------------------------------   

    @commands.command(aliases = ["rank", "lvl"])
    async def level(self, ctx, user: discord.User = None):
        account = server_rank.fetch(ctx.author)
        if user is None:
            user = ctx.author
        elif user is not None:
            user = user
            
        level_card = discord.Embed(title=f"{ctx.author.display_name}'s Level and Experience", color = col)
        level_card.set_thumbnail(url=ctx.author.display_avatar.url)
        level_card.add_field(name = "Level: ", value=account.Level)
        level_card.add_field(name = "Experience: ", value=account.Experience)
        level_card.set_footer(text=f"Requested by {ctx.author.name}")
        
        await ctx.send(embed = level_card)
        
# * -------------------------------------------------------------------   

async def setup(bot):
    await bot.add_cog(LevelSystem(bot))
