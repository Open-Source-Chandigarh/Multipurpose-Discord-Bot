import discord
from discord.ext import commands
import settings
import wavelink             # fully asynchronous API that's intuitive and easy to use with built in Spotify Support and Node Pool Balancing; WORKS WITH LAVALINK TO CREATE SERVERS IN DOCKER



col = discord.Color.purple()

class Music(commands.Cog):
    node = None
    vc : wavelink.Player = None
    current_trek = None
    music_channel = None
    Author = None

    def __init__(self, bot):
        self.bot = bot
        self.history = list()

    async def setup(self):
       node = wavelink.Node(           # Represents a connection to the LavaLink Server
            # bot = self.bot,
            # host = "localhost",
            # port = 2333,           # Default port
            uri="localhost:2333",
            password = "Logic_Link",
            
        )
       await wavelink.NodePool.connect(client=self.bot, nodes=[node])          # Connects to the LavaLink Server

# * -------------------------------------------------------------------   

    @commands.Cog.listener()               # Tells that the bot has connected to a vc
    async def on_wavelink_node_ready(self, node: node):
        print(f"{node} is ready")
    
# * -------------------------------------------------------------------   

    @commands.Cog.listener()             
    async def on_wavelink_track_start(self, payload):
        embed = discord.Embed(
            description=f"Started playing - {self.current_trek} ",
            color = col
        )
        embed.set_footer(text=f"Requested by {self.Author}")
        await self.music_channel.send(embed = embed)
        
# * -------------------------------------------------------------------   

    @commands.Cog.listener()             
    async def on_wavelink_track_end(self, payload):
        if payload.track == self.current_trek: return
        
        if not self.vc.queue.is_empty:
            next_track = self.vc.queue.get()
            self.current_track = next_track
            await self.vc.play(next_track)    
              
        embed = discord.Embed(
            description=f"{self.vc.queue.get()} ended",
            color = col
        )
        await self.music_channel.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Check if the bot is in a voice channel
        if self.vc and self.vc.is_connected():
            # Check if the bot's voice channel became empty (excluding the bot)
            if len([m for m in self.vc.channel.members if not m.bot]) == 0:
                await self.vc.disconnect()
                embed = discord.Embed(title="Insufficient user count", description="I have left the voice channel", color=col)
                await self.music_channel.send(embed = embed)
                self.current_trek = None
                self.now_playing_message = None  # Reset the now playing message

# * -------------------------------------------------------------------   
    
    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel          # to check if user is in voice channel
        if channel:
            self.vc = await channel.connect(cls = wavelink.Player)          # walvelink player gives a voice client
            self.music_channel = ctx.message.channel
            embed = discord.Embed(
                description = f"Joined {channel.name}",
                color=col
            )
            embed.set_footer(text=f"Requested by {ctx.author.display_name}")
            await ctx.send(embed = embed)
            self.Author = ctx.author.display_name
        else:
            embed = discord.Embed(
                description = f"No voice channel to connect to. Please either provide one or join one.",
                color=col
            )
            await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.command()
    async def add(self, ctx, *, title : str):              # * means that anything that comes after add command will be given to us as a list input
        chosen_trek = await wavelink.YouTubeTrack.search(title)             # return only first result found in query
        if not chosen_trek:
            embed = discord.Embed(
                description = f"Song not found!",
                color=col
            )
            await ctx.send(embed = embed)
        else:
            self.current_trek = chosen_trek
            self.current_trek = self.current_trek[0]
            embed = discord.Embed(
                description = f"Added {self.current_trek}",
                color=col
            )
            embed.set_footer(text=f"Requested by {ctx.author.display_name}")
            await ctx.send(embed = embed)
            self.vc.queue.put(self.current_trek)
            
# * -------------------------------------------------------------------   

    @commands.command()
    async def play(self, ctx):
        if self.current_trek and self.vc:
            self.current_trek = self.vc.queue.get()
            await self.vc.play(self.current_trek)
        if self.vc.queue.is_empty:
            embed = discord.Embed(
                description = f"Song queue is Empty!",
                color=col
            )
            await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.command(aliases = ["q"])
    async def List(self, ctx):
        if self.vc.queue.is_empty:
            embed = discord.Embed(
                description="The queue is currently empty.",
                color=col
            )
        else:
            queue_list = "\n".join([f"{i+1}. {track}" for i, track in enumerate(self.vc.queue)])
            embed = discord.Embed(
                title="Song Queue",
                description=queue_list,
                color=col
            )
            embed.set_footer(text=f"Requested by {ctx.author.display_name}")

        await ctx.send(embed=embed)

# * -------------------------------------------------------------------    

    @commands.command()
    async def skip(self, ctx):
        if not self.vc.queue.is_empty:
            self.current_track = self.vc.queue.get()
            try:
                await self.vc.play(self.current_track)
            except Exception as e:
                # Handle any exceptions that may occur during playback
                await ctx.send(f"An error occurred while skipping: {str(e)}")
        else:
            embed = discord.Embed(description="There are no more tracks!", color=col)
            await ctx.send(embed=embed)

# * -------------------------------------------------------------------   

    @commands.command()
    async def pause(self, ctx):
        embed = discord.Embed(color=col)
        embed.set_author(name=f"Paused the song.", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)
        await self.vc.pause()

# * -------------------------------------------------------------------   

    @commands.command()
    async def resume(self, ctx):
        embed = discord.Embed(color=col)
        embed.set_author(name=f"Resumed the song.", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)
        await self.vc.resume()

# * -------------------------------------------------------------------   

    @commands.command()
    async def stop(self, ctx):
        await self.vc.stop()

# * ------------------------------------------------------------------- 
  
    @commands.command()
    async def ff(self, ctx, seconds : int):
        pos = self.vc.position + (seconds*1000)
        await self.vc.seek(pos)            # because seek takes milliseconds as input
  
# * ------------------------------------------------------------------- 
  
    @commands.command()
    async def bw(self, ctx, seconds : int):
        pos = self.vc.position - (seconds*1000)
        await self.vc.seek(pos)
  
# * -------------------------------------------------------------------   

    @commands.command(aliases = ["vol"])
    async def volume(self, ctx, new_vol : int):
        await self.vc.set_volume(new_vol)

# * -------------------------------------------------------------------    

async def setup(bot):
    await bot.add_cog(Music(bot))
    await Music(bot).setup()             # Separating Music setup from cog
