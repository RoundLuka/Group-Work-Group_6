import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.all() 

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("Bot named Andria's Bot is now ready to use")
    print("------------------------------------------")

    await bot.tree.sync()


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1265012166180999311) 
    await channel.send("Hello my name is Andria Lezhava :wave:, Nice to meet you")
    print("Member joined successfully welcomed")

# Farewell members who leave
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1265012166180999311) 
    await channel.send("Goodbye!")
    print("Member left, successfully sent goodbye")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello Andria Lezhava is here!, How can I help you today?")

@bot.command()
async def call(ctx):
    await ctx.send("Calling...")

@bot.command()
async def joke(ctx):
    await ctx.send("Why don’t scientists trust atoms? Because they make up everything! 😄")
@bot.command()
async def commands(ctx):
    await ctx.send("These are the commands you can use: /members, /hello, /call, /joke")


#events

#member join
#member leave

#/commands
#/hello
#/call
#/joke


# Token
bot.run('')

