import settings
import discord
from discord.ext import commands
import json
import database
import openai
from models.account import Account
from models.player_stats import Stats
from models.server_rank import server_rank
from models.warn_system import Warn_system


col = discord.Color.purple()

database.economy_account_db.create_tables([Account])
database.stats_db.create_tables([Stats])
database.server_rank_db.create_tables([server_rank])
database.warn_system_db.create_tables([Warn_system])

intents = discord.Intents.all()

def get_server_prefix(bot, message):
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        return prefix[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_server_prefix, intents=intents)
bot.remove_command("help")

# * -------------------------------------------------------------------
# * -------------------------------------------------------------------


# Handling error            
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, openai.RateLimitError):                             # isinstance checks if the error is caused by the provided reason or not; isinstance is used to check if given value is originating from provided package item or is originating as an instance of provided package item
        embed = discord.Embed(
            title="Rate limit exceeded!",
            description="Usage of time command is limited to 1 person at a time",
            color=col
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):                                # isinstance checks if the error is caused by the provided reason or not; isinstance is used to check if given value is originating from provided package item or is originating as an instance of provided package item
        await ctx.send(f"```Error: Arguments are not provided \n\nFor more info on a specific command, use {'*help*'} command```")
    elif isinstance(error, commands.CommandOnCooldown):
        remaining_time = divmod(error.retry_after, 3600)                  # retry_after contains the remaining time in seconds that we are getting in hours by dividing them by 3600
        if int(remaining_time[0])>=1:
            remaining_time_str = f"{int(remaining_time[0])} hours"
        elif int(remaining_time[0])<1:
            remaining_time = divmod(error.retry_after, 60)                  # retry_after contains the remaining time in seconds that we are getting in minutes by dividing them by 60
            remaining_time_str = f"{int(remaining_time[0])} minutes"
        embed = discord.Embed(
            title="Command on cooldown!",
            description=f"You can use this command again in **{remaining_time_str}**",
            color=col
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"```Error occured during execution\n\nFor more info on a specific command, use {'*help*'} command```")
        raise error


# * -------------------------------------------------------------------
# * -------------------------------------------------------------------


@bot.event                                   # Bot decorator telling it is an event 
async def on_ready():
    print(bot.user)
    print(bot.user.id)
    print("____________________________________________________________")
    
    for cmd_file in settings.cmds.glob("*.py"):                                   # yields all existing files of specified type
        if cmd_file != "__init__.py":
            await bot.load_extension(f"cogs.{cmd_file.stem}")                     # .stem provides file name without extension
    await bot.tree.sync()                                                         # Used to add slash commands 


# * -------------------------------------------------------------------   


    @bot.event
    async def on_guild_join(guild):
# * -------------------------------------------------------------------   
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        prefix[str(guild.id)] = "!"
        with open("cogs/json/prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)
# * -------------------------------------------------------------------   
        with open("cogs/json/mutes.json", "r") as f:
            mute_role = json.load(f)
            mute_role[str(guild.id)] = None
        with open("cogs/json/mutes.json", "w") as f:
            json.dump(mute_role, f, indent = 4)
            
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------


    @bot.event
    async def on_guild_remove(guild):
# * -------------------------------------------------------------------  
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        prefix.pop(str(guild.id))
        with open("cogs/json/prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)
# * -------------------------------------------------------------------   
        with open("cogs/json/mutes.json", "r") as f:
            mute_role = json.load(f)
            mute_role.pop(str(guild.id))
        with open("cogs/json/mutes.json", "w") as f:
            json.dump(mute_role, f, indent = 4)         
# * -------------------------------------------------------------------

        
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="!help"))
    
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------

if __name__ == "__main__":
    bot.run(settings.DISCORD_API_TOKEN) 
 