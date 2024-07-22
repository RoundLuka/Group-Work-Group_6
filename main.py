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
    channel = client.get_channel(1264154912065982518)
    await channel.send("Hello")
    print("Member joined successfuly welcomed")

#leave
@client.event
async def on_member_leave(memeber):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Goodbye")
    print("Member left, successfuly sent goodbye")

@client.command()
async def hello(ctx):
    await ctx.send("How can I help you today?")
    
@client.command()
async def call(ctx):
    await ctx.send("Ring ring 🔔")



#events

#member join
#member leave

#/commands
#/hello
#/call
#/joke












client.run('')