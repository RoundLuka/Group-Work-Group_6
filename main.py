import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '/',intents=intents)

@client.event
async def on_ready():
    print("Bot named Berdia bekauri is now ready to use")
    print("------------------------")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1265012166180999311)
    await channel.send("Hello my name is Berdia Bekauri :wave:, Nice to meet you")
    print("Member joined successfuly welcomed")

@client.event
async def on_member_leave(member):
    channel = client.get_channel(1265012166180999311)
    await channel.send("Goodbye!")
    print("Member left, successfuly sent goodbye")

@client.command()
async def hello(ctx):
    await ctx.send("Hello Berdia Bekauri is here!, How can I help you today?")
    
@client.command()
async def call(ctx):
    await ctx.send("Calling...")


@client.command()
async def joke(ctx):
    await ctx.send("Why don’t scientists trust atoms? Because they make up everything! 😄")

@client.command()
async def commands(ctx):
    await ctx.send("These are the commands you can use: /hello, /call, /joke, /members")

#events

#member join
#member leave

#/commands
#/hello
#/call
#/joke
#/members












client.run('')