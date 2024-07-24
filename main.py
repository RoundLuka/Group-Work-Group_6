import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '/',intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready to use")
    print("------------------------")


#Welcome

@client.event
async def on_member_join(member):
    channel = client.get_channel(1265012166180999311)
    await channel.send("Hello")
    print("Member joined successfuly welcomed")

#leave
@client.event
async def on_member_leave(memeber):
    channel = client.get_channel(1265012166180999311)
    await channel.send("Goodbye")
    print("Member left, successfuly sent goodbye")

@client.command()
async def hello(ctx):
    await ctx.send("How can I help you today?")
    
@client.command()
async def call(ctx):
    await ctx.send("Ring ring 🔔")

@client.command()
async def joke(ctx):
    await ctx.send("kaci shedis saxinkleshi")

@client.command()
async def commands(ctx):
    await ctx.send("these are the commands you can use: /hello, /call, /joke")

@client.command()
async def check(ctx):
    await ctx.send("yes this code is correct!")



#events

#member join
#member leave

#/commands
#/hello
#/call
#/joke
#/check












client.run('')