import discord 
import asyncio
from discord.ext import commands
import json
from models.warn_system import Warn_system


col = discord.Color.purple()
timeout = 10

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot            
        
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, count: int):
        await ctx.channel.purge(limit = count+1)
        embed = discord.Embed(title=f"{count} message(s) have been deleted", color=col)
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        
        message = await ctx.send(embed = embed)
        message
        await asyncio.sleep(timeout)
        await message.delete()
    
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.kick(member)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=col
        )
        conf_embed.add_field(name="Kicked", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)   
        conf_embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = conf_embed)
           
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.ban(member)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=col
        )
        conf_embed.add_field(name="Banned", value=f"{member.mention} has been banned from the server by {ctx.author.mention}", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)   
        conf_embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = conf_embed)
           
# * -------------------------------------------------------------------
   
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, userId):
        user = discord.Object(id = userId)
        await ctx.guild.unban(user)
        
        conf_embed = discord.Embed(
            title=f"Success!",
            color=col
        )
        conf_embed.add_field(name="Unbanned", value=f"<@{userId}> has been unbanned from the server by {ctx.author.mention}", inline=False)
        await ctx.send(embed = conf_embed)   

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def setmuterole(self, ctx, role: discord.Role):
        with open("cogs/json/mutes.json", "r") as f:
            mute_role = json.load(f)
            mute_role[str(ctx.guild.id)] = role.name
        with open("cogs/json/mutes.json", "w") as f:
            json.dump(mute_role, f, indent = 4)
            
        conf_embed = discord.Embed(
            title=f"Success!",
            color=col
        )
        conf_embed.add_field(name="Mute role has been set", value=f"The mute role has been changed to `{role.mention}` for this guild. All members equiped with this role will be muted!", inline=False)
        await ctx.send(embed = conf_embed)

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member):
        with open("cogs/json/mutes.json", "r") as f:
            role = json.load(f)
            mute_role = discord.utils.get(ctx.guild.roles, name = role[str(ctx.guild.id)])            # Getting guild roles from person that ran the command and looking for name of the role that matches the name in json file

        await member.add_roles(mute_role)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=col
        )
        conf_embed.add_field(name="Muted", value=f"{member.mention} has been muted by {ctx.author.mention}.", inline=False)
        await ctx.send(embed = conf_embed)
        
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):
        with open("cogs/json/mutes.json", "r") as f:
            role = json.load(f)
            mute_role = discord.utils.get(ctx.guild.roles, name = role[str(ctx.guild.id)])            # Getting guild roles from person that ran the command and looking for name of the role that matches the name in json file

        await member.remove_roles(mute_role)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=col
        )
        conf_embed.add_field(name="Unmuted", value=f"{member.mention} has been unmuted by {ctx.author.mention}.", inline=False)
        await ctx.send(embed = conf_embed)
        
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def lock(self, ctx, *, reason):
        channel = ctx.channel
        overwrite =channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)
        
        embed = discord.Embed(
            title="🔒 Locked",
            color=col
        )
        embed.add_field(name="Reason", value=reason)
        
        await ctx.send(embed = embed)
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unlock(self, ctx):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)
        
        embed = discord.Embed(
            title="🔓 Unlocked",
            color=col
        )
                
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def lock_server(self, ctx):
        guild = ctx.guild
        channels = guild.text_channels
            
        for channel in channels:
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.view_channel = False
            await channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unlock_server(self, ctx):
        guild = ctx.guild
        channels = guild.text_channels
            
        for channel in channels:
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.view_channel = True
            await channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def warn(self, ctx, member: discord.Member, reason):
        account = Warn_system.fetch(ctx.author)
        account.warns+=1
        account.save()
        
        if int(account.warns) < 5:
            embed = discord.Embed(
                title="Warning!",
                description=f"{member.display_name} has been warned by {ctx.author}",
                color=col
            )
            embed.set_author(name="Warning", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name="Reason", value=reason, inline=False)
            embed.add_field(name="Total warns", value=account.warns, inline=False)
        
        else:
            await ctx.guild.kick(member)
            embed = discord.Embed(
                title="Warning Limit Reached!",
                description=f"{member.display_name}'s warn limit has been reached and now has been kicked out of the server!"
            )
            embed.set_author(name="Warning", icon_url=ctx.author.display_avatar.url)
            account.warns = 0
            account.save()
        
        
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------

    @commands.command(aliases = ["rw"])
    @commands.has_permissions(administrator = True)
    async def remove_warn(self, ctx, member: discord.Member, amount = 0):
        account = Warn_system.fetch(ctx.author)
        
        if amount == 0:
            account.warns = 0
            account.save()
            embed = discord.Embed(
                title="Removed all warns!",
                description=f"{member.display_name}'s warns have been removed",
                color=col
            )
            embed.set_author(name="Warns Removed", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name="Total warns", value=account.warns, inline=False)
        
        elif amount>account.warns:
            embed = discord.Embed(
                title="Amount provided is greater than warns",
                color=discord.Color.red()
            )
            embed.set_author(name="Amount error", icon_url=ctx.author.display_avatar.url)
            
        else:
            account.warns -= amount
            account.save()
            embed = discord.Embed(
                title=f"Removed {amount} warn(s)!",
                description=f"{member.display_name}'s warns have been removed",
                color=col
            )
            embed.set_author(name="Warns Removed", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name="Total warns left", value=account.warns, inline=False)

        
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------

    @commands.command(aliases = ["vw"])
    @commands.has_permissions(administrator = True)
    async def view_warns(self, ctx, member: discord.Member):
        account = Warn_system.fetch(ctx.author)

        embed = discord.Embed(
            title=f"{member.display_name}'s Warns",
            color=col
        )
        embed.set_author(name="Warns", icon_url=ctx.author.display_avatar.url)
        embed.add_field(name="Total warns left", value=account.warns, inline=False)
        
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Moderation(bot))
    
    