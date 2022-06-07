import discord
from discord.ext import commands

TOKEN = 'Your Discord Bot Token'

description = '''Python Discord Bot'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    await ctx.send("world")

bot.run(TOKEN)
