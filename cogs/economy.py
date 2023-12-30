import discord 
import random
import peewee
from discord.ext import commands
from models.account import Account


col = discord.Color.purple()

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# * -------------------------------------------------------------------   

    @commands.command(aliases = ["cf"])
    async def cflip(self, ctx, choice: str, amount: int):
        account = Account.fetch(ctx.author)
        if amount > account.cash:
             embed = discord.Embed(
                description=f"You do not have enough credits!... Please withdraw from bank or use some oter commands",
                color=col
            )
        
        heads = random.randint(0,1)            # 0 means tails and 1 means heads
        won = False
        if heads and choice.lower().startswith("h"):
            won = True
            account.cash += amount
        elif not heads and choice.lower().startswith("t"):
            won = True
            account.cash += amount
        else:
            account.cash -= amount
        
        account.save()
        if won:
            embed = discord.Embed(
                title=f"**{ctx.author.display_name}** has won the coin flip ^o^!",
                description=f"Your current balance: {account.cash}",
                color=discord.Color.green()
            )
            embed.set_author(name='Coin Flip')
            embed.set_footer(text = "This command doesn't have any cooldown")
        
        if not won:
            embed = discord.Embed(
                title=f"**{ctx.author.display_name}** just lost the coin flip... :c!",
                description=f"Your current balance: {account.cash}",
                color=discord.Color.red()
            )
            embed.set_author(name='Coin Flip')
            embed.set_footer(text = "This command doesn't have any cooldown")
        
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.command(aliases = ["bal"])
    async def balance(self, ctx):
        account = Account.fetch(ctx.author)
        embed = discord.Embed(
            title=f"{ctx.author.display_name}'s Current Balance",
            description=f"The current balance of this user.",
            color=col
        )
        embed.add_field(name="Cash:", value=f"**{account.cash}**", inline=True)
        embed.add_field(name="Bank:", value=f"**{account.bank}**", inline=True)
        embed.add_field(name="Net Worth:", value=f"**{account.cash + account.bank}**", inline=True)
        embed.set_footer(text="Want to increase balance? Try running some economy based commands")
        embed.set_thumbnail(url = ctx.author.display_avatar.url)

        await ctx.send(embed = embed)
        
# * -------------------------------------------------------------------   

    @commands.cooldown(1, per = 600)
    @commands.command()
    async def beg(self, ctx):
        account = Account.fetch(ctx.author)
        
        change_val = random.randint(-50, 100)
        prev = account.cash
        account.cash += change_val
        
        account.save()
        
        if account.cash < prev:
            embed = discord.Embed(
                title=f"Oh No! - You have been robbed!",
                description=f"A group of robbers saw oppertunity in taking advantage of you.",
                color=discord.Color.red()
            )
            embed.add_field(name="Amount robbed:", value=f"**{abs(change_val)}**", inline = False)
            embed.add_field(name="New Balance:", value=f"**{account.cash}**", inline = False)
            embed.set_footer(text="Should probably beg in a nicer part of town...")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
            
        elif account.cash > prev:
            embed = discord.Embed(
            title=f"Oh Sweet Green!",
                description=f"Some kind souls have given you what they could.",
                color=discord.Color.green()
            )
            embed.add_field(name="Amount gained:", value=f"**{change_val}**", inline = False)
            embed.add_field(name="New Balance:", value=f"**{account.cash}**", inline = False)
            embed.set_footer(text="Want more? Wait 10 minutes to run this command again, or try some other commands!")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
            
        elif account.cash == prev:
            embed = discord.Embed(
            title=f"Awh That Sucks!",
                description=f"Looks like begging didn't get you anywhere today",
                color=discord.Color.green()
            )
            embed.add_field(name="Amount gained:", value=f"**{change_val}**", inline = False)
            embed.add_field(name="New Balance:", value=f"**{account.cash}**", inline = False)
            embed.set_footer(text="Want more? Wait 10 minutes to run this command again, or try some other commands!")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.cooldown(1, per = 3600)
    @commands.command()
    async def work(self, ctx):
        account = Account.fetch(ctx.author)
        paid = random.randint(200, 500)
        account.cash += paid
        account.save()
        
        embed = discord.Embed(
            title="Phew!",
            description="After a tiring shift, here's your earning!",
            color=discord.Color.green()
        )
        embed.add_field(name="Earnings:", value=f"**{paid}**", inline=False)
        embed.add_field(name="New Balance:", value=f"**{account.cash}**")
        embed.set_footer(text="Want more? Wait 1 hour to run this command again, or try some other commands!")
        embed.set_thumbnail(url = ctx.author.display_avatar.url)
        await ctx.send(embed = embed)
        
# * -------------------------------------------------------------------  

    @commands.command(aliases = ["dep"])
    async def deposit(self, ctx, amount: int):
        account = Account.fetch(ctx.author)
        
        if amount<=account.cash:
            account.bank += amount
            account.cash -= amount
            account.save()
            embed = discord.Embed(
                title="Deposited!",
                description="You just deposited cash in your bank!",
                color=col
            )
            embed.add_field(name="Amount Deposited:", value=f"**{amount}**")
            embed.add_field(name="Amount in bank:", value=f"**{account.bank}**")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        
        elif amount>account.cash:
            account.bank += account.cash
            account.cash = 0
            account.save()
            embed = discord.Embed(
                title="Deposited!",
                description="You have deposited all your cash in your bank account!",
                color=col
            )
            embed.add_field(name="Balance:", value=f"**{account.cash}**")
            embed.add_field(name="Amount in bank:", value=f"**{account.bank}**")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)            

# * -------------------------------------------------------------------  

    @commands.command(aliases = ["wd"])
    async def withdraw(self, ctx, amount: int):
        account = Account.fetch(ctx.author)
        
        if amount<=account.bank:
            account.bank -= amount
            account.cash += amount
            account.save()
            embed = discord.Embed(
                title="Amount withdrawn!",
                description="You just withdrawed cash from your bank!",
                color=col
            )
            embed.add_field(name="Amount withdrawn:", value=f"**{amount}**", inline=False)
            embed.add_field(name="Amount in cash:", value=f"**{account.cash}**", inline = True)
            embed.add_field(name="Amount in bank:", value=f"**{account.bank}**", inline = True)
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
        
        elif amount>account.bank:
            embed = discord.Embed(
                title="Low Bank Amount!",
                description="You don't have enough credits in your bank account!",
                color=col
            )
            embed.add_field(name="Balance:", value=f"**{account.cash}**")
            embed.add_field(name="Amount in bank:", value=f"**{account.bank}**")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)            


# * -------------------------------------------------------------------  

    @commands.cooldown(1, per=3600)
    @commands.command()
    async def steal(self, ctx, member: discord.Member):
        account_user = Account.fetch(ctx.author)
        account_member = Account.fetch(member)
        steal_probability = random.choice([0,1])
        
        if steal_probability == 1:          # User gets to steal
            
            if account_member.cash > 0:
                val = 0.8 * float(account_member.cash)
                robbed = random.randrange(1, int(val))
                account_user.cash += robbed
                account_member.cash -= robbed
                account_user.save()
                account_member.save()
                
                embed = discord.Embed(
                title="Success!",
                description="You had a successful robbery!",
                color=discord.Color.green()
                )
                embed.add_field(name="Earnings:", value=f"**{robbed}**", inline=False)
                embed.add_field(name="New Balance:", value=f"**{account_user.cash}**")
                embed.set_footer(text="Want more?.. Wait 1 hour to run this command again, or try some other commands!")
                embed.set_thumbnail(url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed)
            elif account_member.cash <= 0:
                embed = discord.Embed(
                title="Not enough to steal",
                description="Mentioned user doesn't have enough cash to steal!",
                color=discord.Color.red()
                )
                embed.set_footer(text="Better luck next time I guess")
                embed.set_thumbnail(url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed)
            
        elif steal_probability == 0:
            if account_user.cash>0:
                val = 0.3 * float(account_user.cash)
                caught = random.randrange(0, int(val))
                
                account_user.cash -= caught
                account_member.cash += caught
                account_user.save()
                
                embed = discord.Embed(
                title="Uh oh!",
                description="You got caught while stealing and are now forced to pay back to member!",
                color=discord.Color.red()
                )
                embed.add_field(name="Penalities:", value=f"**{caught}**", inline=False)
                embed.add_field(name="New Balance:", value=f"**{account_user.cash}**")
                embed.set_footer(text="Better luck next time I guess")
                embed.set_thumbnail(url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed)
            elif account_user.cash <=0:
                val = 0.3 * float(account_user.bank)
                caught = random.randrange(0, int(val))
                
                account_user.bank -= caught
                account_member.cash += caught
                account_user.save()
                
                embed = discord.Embed(
                title="Uh oh!",
                description="You got caught while stealing and are now forced to pay back to member!",
                color=discord.Color.red()
                )
                embed.add_field(name="Penalities:", value=f"**{caught}**", inline=False)
                embed.add_field(name="Cash:", value=f"**{account_user.cash}**", inline=True)
                embed.add_field(name="Bank:", value=f"**{account_user.bank}**", inline=True)
                embed.set_footer(text="Better luck next time I guess")
                embed.set_thumbnail(url = ctx.author.display_avatar.url)
                await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.cooldown(1, per=86400)
    @commands.command()
    async def daily(self, ctx):
        account = Account.fetch(ctx.author)
        
        
        
        daily_coins_prev = ((account.daily_days - 1) * 250) / 5
        daily_coins = (account.daily_days * 250) / 5
        account.cash += daily_coins
        account.daily_days += 1
        account.save()
        embed = discord.Embed(
            title=f"{ctx.author.display_name}'s daily credits",
            description=f"Daily credits were placed in your account",
            color=col
        )
        embed.add_field(name="Daily coins:", value=f"**{daily_coins}**", inline=True)
        embed.add_field(name="Daily Streak:", value=f"**{account.daily_days - 1}**", inline=True)
        embed.add_field(name="Daily Streak bonus:", value=f"**{daily_coins - daily_coins_prev}**", inline=True)
        embed.add_field(name="Cash:", value=f"**{account.cash}**", inline=True)
        embed.add_field(name="Bank:", value=f"**{account.bank}**", inline=True)
        embed.set_footer(text="Streak increases the amount of coins you get per day, so maintain it!")
        embed.set_thumbnail(url = ctx.author.display_avatar.url)
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------   
        
        
async def setup(bot):
    await bot.add_cog(Economy(bot))
    