import discord
from discord.ext import commands
from datetime import datetime
import json



col = discord.Color.purple()

async def is_owner(ctx):
    return ctx.author.id == ctx.guild.owner.id

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command ()
    async def invite(self, ctx):
        a = "__frostxd"
        embed = discord.Embed(
            colour=col,
            description=f"""Hello. I am **Logic Link**, a multipurpose bot built by **{a}**.
            You can add me to your server with the link below:
            
            [Click to add me in your server!](https://discord.com/api/oauth2/authorize?client_id=1154012892258115606&permissions=8&scope=bot)"""
        )
        
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(url="https://i.imgur.com/ggG1PXy.png")
        
        await ctx.send(embed = embed)                  
          
# * -------------------------------------------------------------------   

    @commands.command(aliases = ["sp"])
    async def setprefix(self, ctx, *, newprefix: str):
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        
        prefix[str(ctx.guild.id)] = newprefix
        
        with open("cogs/json/prefixes.json", "w") as f:
            json.dump(prefix, f, indent=4)
     
# * -------------------------------------------------------------------   
        
    @commands.command ()
    async def joined(self, ctx, who : discord.Member = None):
        if who is None:
            joined_at = ctx.author.joined_at.strftime("%Y-%m-%d at %H:%M")
            embed = discord.Embed(
                colour=col,
                title=f"{ctx.author.display_name} joined on {joined_at}"                        # display_name displays the server name of the author not their tag name   
            )
        else:
            joined_at = who.joined_at.strftime("%Y-%m-%d at %H:%M")
            embed = discord.Embed(
                colour=col,
                title=f"{who.display_name} joined on {joined_at}"                        # display_name displays the server name of the author not their tag name   
            )
        
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed = embed)                  
          
# * -------------------------------------------------------------------   
    
    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, cog: str):
        try: 
            self.bot.load_extension(f"cogs.{cog.lower()}")
            await ctx.send(f"```Loaded cog: {cog}```")
        except commands.ExtensionNotFound:
            await ctx.send(f"```Cog not found: {cog}```")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f"```Cog already loaded: {cog}```")
    
# * -------------------------------------------------------------------   
       
    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, cog: str):
        try:
            await self.bot.unload_extension(f"cogs.{cog.lower()}")
            await ctx.send(f"```Unloaded cog: {cog}```")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"```Cog not loaded: {cog}```")

        
# * -------------------------------------------------------------------   
       
    @commands.command(aliases = ["user", "stats"])
    async def userinfo(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
        elif member is not None:
            member = member
            
        embed = discord.Embed(
            title=f"{member.display_name}'s User Information",
            description="All info about the user",
            color=col
        )
        embed.set_author(name="User Info", icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(url=member.display_avatar)
        embed.add_field(name="Name", value=member.name, inline=False)
        embed.add_field(name="Nick Name", value=member.display_name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Top Role", value=member.top_role, inline=False)
        embed.add_field(name="Status", value=member.status, inline=False)
        embed.add_field(name="Bot User", value=member.bot, inline=False)
        embed.add_field(name="ID Creation", value=member.created_at.__format__("%A, %d. %B %Y at %H:%M:%S"), inline=False)               # A is day of week; d is day; B is month
        
        await ctx.send(embed=embed)
        
# * -------------------------------------------------------------------   

    # Error handling for load and unload
    @load.error
    @unload.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("```Permission Denied!```")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Missing required argument.```")
        else:
            await ctx.send(f"```An error occurred: {error}```")
        raise error
            
# * -------------------------------------------------------------------   
    

async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))
    
