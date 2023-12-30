import discord
from discord.ext import commands
import random

# Cogs are used to make categories

col = discord.Color.purple()

class Actions(commands.Cog):
    
    def footer(self):
        return f"!help fun [command] for more information"

    @commands.group() 
    async def fun(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to fun\n\nFor more info on a specific command, use {'*help*'} command```")

# * -------------------------------------------------------------------   

    @fun.command()
    async def slap(self, ctx, who : discord.Member, *reason):
        li = [
            'https://media.tenor.com/aCZMe2OKWX0AAAAC/fail-water.gif',
            'https://media.tenor.com/pUatwfgNCZUAAAAd/fish-slap-w2s.gif',
            'https://media.tenor.com/pmCZDX1MB1gAAAAC/johnny-knoxville-slap.gif',
            'https://media.tenor.com/83tH-nXQeAMAAAAC/fish-slap.gif',
            'https://media.tenor.com/-RSry4HDatUAAAAC/slap-out-kast.gif',
            'https://media.tenor.com/__oycZBexeAAAAAC/slap.gif',
            'https://media.tenor.com/WsKM5ZDigvgAAAAC/penguin-penguins.gif',
            'https://media.tenor.com/tKF3HiguDmEAAAAC/wrrruutchxxxxiii-slapt.gif',
            'https://media.tenor.com/2L_eT6hPUhcAAAAC/spongebob-squarepants-patrick-star.gif',
            'https://media.tenor.com/fw6gs_ia_UIAAAAd/slap-slapping.gif',
            'https://media.tenor.com/OXFdOzVbsW0AAAAC/smack-you.gif',
            'https://media.tenor.com/R6LaPVpPwfcAAAAd/slap-slapping.gif',
            'https://media.tenor.com/zdNVA6sB53AAAAAC/molorant-ckaz.gif',
            'https://media.tenor.com/E3OW-MYYum0AAAAC/no-angry.gif',
            'https://media.tenor.com/2-r7BEc-cb8AAAAC/slap-smack.gif',
            'https://media.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif',
            'https://media.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif',
            'https://media.tenor.com/5jBuDXkDsjYAAAAC/slap.gif',
            'https://media.tenor.com/eU5H6GbVjrcAAAAC/slap-jjk.gif',
            'https://media.tenor.com/0yMtzZ0GUGsAAAAC/hyouka-good.gif'
        ]
        
        embed = discord.Embed(
            colour=col,
            title=f"{ctx.author.display_name} slaps {who.display_name} for being {' '.join(reason)}"
        )
        embed.set_author(name = ctx.author.display_name ,icon_url=ctx.author.display_avatar.url)
        embed.set_image(url=random.choice(li))
        await ctx.send(embed=embed)
        
# * -------------------------------------------------------------------   

    @fun.command ()
    async def say(self, ctx, *what):
        embed = discord.Embed(
            colour=col,
            # description=,
            title=" ".join(what)                            # bot will send the same message as user
        )
        
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        # embed.set_footer(text=self.footer())
        # embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
        await ctx.send(embed = embed)            

# * -------------------------------------------------------------------   

    @fun.command ()
    async def choice(self, ctx, *options):
        embed = discord.Embed(
            color=col,
            title="I'll be choosing ",
            description=random.choice(options)+"!"
        )
        
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)   

# * -------------------------------------------------------------------   
# * -------------------------------------------------------------------   
    
     
async def setup(bot):
    await bot.add_cog(Actions(bot))
